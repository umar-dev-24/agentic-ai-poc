from autogen import AssistantAgent

def create_report_writer_agent(config):
    return AssistantAgent(
        name="ReportWriter",
        llm_config={"config_list": config},
        system_message=(
            "You are a report formatter. You take an executive summary and format it into a markdown report. "
            "Include a title, a short 3–4 line summary, and a concise conclusion. Do not exceed 6 lines. "
            "End your message with 'Final Report Complete.'"
        ),
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: "Final Report Complete" in msg.get("content", ""),
        default_auto_reply="Done.",
        max_consecutive_auto_reply=1,
        code_execution_config=False,
    )
