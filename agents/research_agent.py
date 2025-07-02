from autogen import AssistantAgent

def create_research_agent(config):
    return AssistantAgent(
        name="Researcher",
        llm_config={"config_list": config},
         system_message="""You are a research agent. Given a topic from your knowledge give points on the topic
            Limit your response to a maximum of 600 words, not more than that strictly.
            Make it structured and readable. End your message with 'research completed'.""",
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: msg.get("content", "").strip().endswith("Research Complete."),
        max_consecutive_auto_reply=1,
        default_auto_reply="Passing research findings to the summarizer.",
        code_execution_config=False,
    )
