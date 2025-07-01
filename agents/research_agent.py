from autogen import AssistantAgent

def create_research_agent(config):
    return AssistantAgent(
        name="Researcher",
        llm_config={"config_list": config},
        system_message="You are a research agent. Given a topic, find relevant information from the web "
            "or your knowledge and present it concisely. Limit your response to a maximum of 10 lines. "
            "Make it structured and readable. End your message with research completed.",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").endswith("Done."),
        default_auto_reply="Passing research findings to the summarizer.",
        max_consecutive_auto_reply=1,
        code_execution_config=False,
    )
