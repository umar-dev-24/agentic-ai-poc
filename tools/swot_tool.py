from langchain.tools import Tool
import requests


def swot_analysis_tool_func(company_name: str) -> str:
    prompt = (
        f"Perform a SWOT analysis of the company {company_name}. "
        "Return exactly 2 points for each: Strengths, Weaknesses, Opportunities, and Threats. "
        "Format:\nStrengths:\n- ...\n- ...\nWeaknesses:\n- ...\n- ...\nOpportunities:\n- ...\n- ...\nThreats:\n- ...\n- ..."
    )
    url = "http://localhost:11434/v1/completions"
    payload = {"model": "mistral", "prompt": prompt, "max_tokens": 512, "stream": False}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()


swot_analysis_tool = Tool(
    name="SWOTAnalysisTool",
    func=swot_analysis_tool_func,
    description="Performs SWOT analysis on a given company using local Mistral LLM. Returns 2 points for each SWOT category.",
)
