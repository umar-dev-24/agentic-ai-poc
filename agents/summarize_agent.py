from autogen import ConversableAgent
from llm.gemini_llm import llm_config_gemini


def create_summarizer_agent():
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

    print("Loaded LLM Config for summarizer:", mistral_config)

    return ConversableAgent(
        name="SummarizerAgent",
        llm_config=mistral_config,
        system_message=(
            """ You are one of the agent in multi agentic AI group. You will be given results of research and analysis report of a company and asked to do a summarize that. Your job is to do a summarize that precisely without loosing major points.You should do your task only when you have research agent's result and SWOT's results.your summary should be less than 200 words. Send your results once you are done and finish with a message 'My part is done'. If you are assigned the same task again and again, reject by saying I already did this task and I replied please check. you will be called by co ordinator agent to do the task in the group chat. You should do the task assigned and destined to you, do not talk unnecessarily"""
        ),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=5,
        code_execution_config=False,
    )
