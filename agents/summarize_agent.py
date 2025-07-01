from autogen import AssistantAgent

def create_summarizer_agent(config):
    return AssistantAgent(
        name="Summarizer",
        llm_config={"config_list": config},
        system_message=(
            "You summarize the research clearly and concisely. Create an executive-level summary "
            "with a maximum of 5 lines. Avoid repetition and include only important points. "
            "End your message with 'Summary Complete.'"
        ),
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: "Summary Complete" in msg.get("content", ""),
        default_auto_reply="Summary Complete.",
        max_consecutive_auto_reply=1,
        code_execution_config=False,
    )
