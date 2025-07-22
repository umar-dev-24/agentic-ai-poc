from agents.research_agent import create_research_agent
from agents.analyst_agent import create_analyst_agent
from agents.summarize_agent import create_summarizer_agent
from agents.db_agent import create_db_agent, get_summary, store_summary
from tools.web_search_tool import duckduckgo_search

# from tools.web_search_tool import duckduckgo_tool
from tools.swot_tool import swot_analysis_tool
from autogen import ConversableAgent, GroupChat, GroupChatManager
import streamlit as st
import os
from config import API_KEY
from llm.gemini_llm import llm_config_gemini

# External config for LLMs

mistral_llm_config = {
    "config_list": [
        {
            "model": "mistral",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "api_type": "openai",
        }
    ]
}

gemini_llm_config = {
    "config_list": [
        {
            "model": "gemini-2.0-flash",
            "api_key": API_KEY,  # ✅ Replace this or load from env
            "base_url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
            "api_type": "google",
            "price": [0.0, 0.0],  # Optional to suppress cost warnings
        }
    ]
}


def main():
    st.set_page_config(page_title="Agentic Market Analyzer", layout="wide")
    st.title("📊 Agentic AI - Company Market Intelligence- AUTOGEN")

    company = st.text_input("Enter a company name to analyze", "")
    submit = st.button("Analyze")

    if submit and company:
        user_prompt = f" Get the latest activities and SWOT analysis of  company: {company}. And prepare a executive summary based on the details you gather."
        with st.spinner("🔍 Checking database..."):
            cached = get_summary(company)

        if cached:
            st.success("✅ Found summary in database.")
            st.markdown(cached)
        else:
            with st.spinner("🧠 Running multi-agent analysis..."):
                try:
                    print("\n🚀 [DEBUG] Creating agents...")
                    research_agent = create_research_agent()
                    print("✅ [DEBUG] ResearchAgent created")
                    analyst_agent = create_analyst_agent()
                    print("✅ [DEBUG] AnalystAgent created")
                    summarizer_agent = create_summarizer_agent()
                    print("✅ [DEBUG] SummarizerAgent created")

                    from autogen import UserProxyAgent

                    print("[DEBUG] Import UserProxyAgent")
                    coordinator_agent = ConversableAgent(
                        name="CoordinatorAgent",
                        llm_config=gemini_llm_config,  # ✅ No config_list, no api_type
                        functions=[],
                        system_message=(
                            """You are the coordinator agent.
                                Your job is to read the instruction given to you and complete it using agents that are available based on its capability.
                                Analyse the sentence or company name provided by the user and decide which agents to call based on the information needed.
                                If you cant find a company name in input or input is irrelevant to any company then return 'Sorry I cant do that.'
                                Based on the user input use the following if needed:Use the Research Agent to research about company and to get latest info, the Analyse Agent for SWOT analysis, and the Summarize Agent for drafting executive summary using other agents results.
                                Once all agents are replied with their results and you think you have achieved the output for your task means executive summary for a company return as your response and end.. 
                                Use them wisely and avoid repetative use of them.
                                Each agent has its own tools and capabilities.
                                Decide the order in which to call the agents , once you are done, return the result.
                                Do not do the task yourselff, split the task and assign to concerned agent and make use of them.
                                Once you are ready with a executive summary, return it as your response with a clear ending message 'task is now complete' from your side.
            
"""
                        ),
                        human_input_mode="NEVER",
                        code_execution_config={"work_dir": ".", "use_docker": False},
                        is_termination_msg=lambda x: "task is now complete"
                        in x.get("content", "").lower(),
                    )
                    print("✅ [DEBUG] CoordinatorAgent created")

                    print("\n📦 [DEBUG] Setting up GroupChat...")
                    groupchat = GroupChat(
                        agents=[
                            coordinator_agent,
                            research_agent,
                            analyst_agent,
                            summarizer_agent,
                        ],
                        max_round=10,
                        admin_name="CoordinatorAgent",
                    )
                    manager = GroupChatManager(
                        groupchat=groupchat,
                        llm_config=gemini_llm_config,  # ✅ No config_list, no api_type
                    )
                    print("[DEBUG] GroupChatManager created")

                    print("\n🧠 [DEBUG] Initiating chat...\n")
                    manager.initiate_chat(coordinator_agent, message=user_prompt)
                    print("[DEBUG] manager.initiate_chat() completed")
                except Exception as e:
                    print(f"\n❌ [ERROR] Exception during groupchat run: {e}")
                    st.error(f"❌ Exception during groupchat run: {e}")
                    return

                # Always show the agent conversation log and summary in the UI after the run
                st.markdown("---")
                st.subheader("🤖 Behind the Scenes: Agent Conversation Log")
                if groupchat.messages:
                    for i, msg in enumerate(groupchat.messages):
                        st.markdown(
                            f"**{i}: [{msg['role']}] {msg.get('name', '')}**<br>{msg['content']}",
                            unsafe_allow_html=True,
                        )
                else:
                    st.info("No agent messages were generated.")

                st.markdown("---")
                st.subheader("📋 Executive Summary")
                if len(groupchat.messages) > 1:
                    last_msg = groupchat.messages[-1]["content"]
                    st.success("✅ Summary generated.")
                    st.markdown(last_msg)
                else:
                    st.warning(
                        "⚠️ No summary was generated. Please check logs for agent errors."
                    )


if __name__ == "__main__":
    main()
