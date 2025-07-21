from duckduckgo_search import DDGS


def duckduckgo_search(query: str, num_results: int = 5) -> str:
    with DDGS() as ddgs:
        print(
            f"🔍 [DEBUG] Searching DuckDuckGo for: {query} (max {num_results} results)"
        )
        results = ddgs.text(query, max_results=num_results)
        return "\n".join(
            [res["body"] for res in results if "body" in res and res["body"]]
        )
