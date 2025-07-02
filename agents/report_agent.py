from autogen import AssistantAgent

def create_report_writer_agent(config):
    return AssistantAgent(
        name="ReportWriter",
        llm_config={"config_list": config},
        system_message = """
        You are a report generation expert. Based on the provided summary, create a final report.
        Only highlight the most critical insights.
        Your entire response must not exceed 70 words strictly.
        Avoid repetition or elaboration. Do NOT provide detailed background or explanations.
        Write in a clear, executive tone suitable for high-level business stakeholders.
        End your reply with the phrase 'Final Report Complete.'
        """,
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").strip().endswith("Done."),
        max_consecutive_auto_reply=1,
        default_auto_reply="Final Report Completed. Done.",
        code_execution_config=False,
    )
