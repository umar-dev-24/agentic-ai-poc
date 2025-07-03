from autogen import ConversableAgent
from tools.web_search_tool import duckduckgo_search, duckduckgo_tool

import os

mistral_config = {
    "config_list": [
        {
            "model": "mistral",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "api_type": "openai",
        }
    ]
}


def create_research_agent():
    from llm.gemini_llm import llm_config_gemini

    agent = ConversableAgent(
        name="ResearchAgent",
        llm_config=mistral_config,  # ✅ No config_list, no api_type
        system_message=(
            """ You are one of the agent in multi agentic AI group. You will be ordered a task and given a company name and asked to do a research on that. Your job is to do a research on that company using the tool given to you. Get the latest activities of that company as part of your research. Send the top 5 results of your research. Send your results once you are done and finish with a message 'My part is done'. If you are assigned the same task again and again, reject by saying I already did this task and I replied please check.you will be called by co ordinator agent to do the task in the group chat. You should do the task assigned and destined to you, do not talk unnecessarily """
        ),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=5,
        code_execution_config=False,
        is_termination_msg=lambda x: False,
    )

    agent.register_function({"duckduckgo_search": duckduckgo_search})
    return agent
