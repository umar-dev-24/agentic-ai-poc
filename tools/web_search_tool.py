from langchain.tools import Tool


def duckduckgo_search(query: str, num_results: int = 5) -> str:
    from duckduckgo_search import DDGS

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=num_results)
        return "\n".join(
            [
                res["body"]
                for res in results
                if "body" in res and res["body"] is not None
            ]
        )


duckduckgo_tool = Tool(
    name="DuckDuckGoSearch",
    func=lambda q: duckduckgo_search(q),
    description="Search the web and get top 3 results for recent information about companies or industries.",
)
