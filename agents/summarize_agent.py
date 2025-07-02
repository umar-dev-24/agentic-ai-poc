from autogen import AssistantAgent

def create_summarizer_agent(config):
    return AssistantAgent(
        name="Summarizer",
        llm_config={"config_list": config},
        system_message=(
            """You summarize the research points given clearly and concisely. Create an executive-level summary 
            with a maximum of 250 words, not more than that strictly. Avoid repetition and include only important points. 
            End your message with 'Summary Completed.'"""
        ),
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: msg.get("content", "").strip().endswith("Summary Complete."),
        max_consecutive_auto_reply=1,
        default_auto_reply="Summary Complete.",
        code_execution_config=False,
    )
