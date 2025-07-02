from autogen import GroupChat, GroupChatManager, UserProxyAgent
from agents.research_agent import create_research_agent
from agents.summarize_agent import create_summarizer_agent
from agents.report_agent import create_report_writer_agent
from llm import get_llm_config

def main():
    config = get_llm_config()

    # Create agents
    researcher = create_research_agent(config)
    summarizer = create_summarizer_agent(config)
    report_writer = create_report_writer_agent(config)

    # User proxy to start the chat
    user_proxy = UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )

    # Create the group chat
    group_chat = GroupChat(agents=[user_proxy, researcher, summarizer, report_writer], messages=[])

    # Controller to manage agent routing
    manager = GroupChatManager(groupchat=group_chat, llm_config={"config_list": config})

    print("=== 🚀 GroupChat Market Analysis Workflow ===")
    user_proxy.initiate_chat(manager, message="Generate a market analysis on the handmade products in India.")

if __name__ == "__main__":
    main()
