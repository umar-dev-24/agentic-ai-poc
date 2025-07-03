from autogen import ConversableAgent
from tools.swot_tool import swot_analysis_tool
from llm.gemini_llm import llm_config_gemini


def create_analyst_agent():
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

    agent = ConversableAgent(
        name="AnalystAgent",
        llm_config=mistral_llm_config,  # ✅ No config_list, no api_type
        system_message=(
            """ You are one of the agent in multi agentic AI group. You will be given a company name and asked to do a SWOT analysis on that. Your job is to do a SWOT analysis on that company using the tool given to you. Get 2 points on each category of SWOT. Send results of your analysis. Send your results once you are done and finish with a message 'My part is done'. If you are assigned the same task again and again, reject by saying I already did this task and I replied please check.you will be called by co ordinator agent to do the task in the group chat. You should do the task assigned and destined to you, do not talk unnecessarily """
        ),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=5,
        code_execution_config=False,
        is_termination_msg=lambda x: False,
    )

    from tools.swot_tool import swot_analysis_tool_func

    agent.register_function({"swot_analysis": swot_analysis_tool_func})
    return agent
