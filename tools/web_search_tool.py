from duckduckgo_search import ddg


def duckduckgo_search(query: str, num_results: int = 5) -> str:
    try:
        print(f"🔍 [DEBUG] Performing DuckDuckGo search for: {query}")
        results = ddg(query, max_results=num_results)
        summaries = [res["body"] for res in results if "body" in res and res["body"]]
        return "\n".join(summaries) if summaries else "No content found."
    except Exception as e:
        return f"Error: DuckDuckGo search failed due to: {str(e)}"
