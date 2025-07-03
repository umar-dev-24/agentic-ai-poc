from autogen import UserProxyAgent
from tinydb import TinyDB, Query

# Setup DB (create if not exists)
db = TinyDB("company_summaries.json")
Company = Query()


def store_summary(company_name: str, summary: str):
    db.upsert(
        {"company": company_name.lower(), "summary": summary},
        Company.company == company_name.lower(),
    )


def get_summary(company_name: str):
    result = db.get(Company.company == company_name.lower())
    if result and isinstance(result, dict):
        return result.get("summary")
    return None


def create_db_agent():
    agent = UserProxyAgent(
        name="DatabaseAgent",
        human_input_mode="NEVER",
        system_message="You store the final summary into the database. Store only the 'summary' field against the given company name.",
        code_execution_config={"work_dir": ".", "use_docker": False},
    )

    agent.register_function({"store_summary": store_summary})
    return agent
