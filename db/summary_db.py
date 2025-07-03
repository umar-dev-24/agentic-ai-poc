from tinydb import TinyDB, Query
from pathlib import Path

# Set path for the DB file
db_path = Path(__file__).parent / "summary_db.json"
db = TinyDB(db_path)
Summary = Query()

def get_summary(company: str) -> str | None:
    result = db.search(Summary.company == company.lower())
    if result:
        return result[0]["summary"]
    return None

def save_summary(company: str, summary: str) -> None:
    db.upsert({"company": company.lower(), "summary": summary}, Summary.company == company.lower())
