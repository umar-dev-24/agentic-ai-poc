from ddgs import DDGS


def duckduckgo_search(query: str, num_results: int = 5) -> str:
    try:
        print(f"🔍 Performing DuckDuckGo search for query: {query}")
        results = DDGS().text(query, max_results=num_results)
        print(f"Search results for query '{query}': {results}")
        if not results:
            return "No relevant search results found."

        # Safely extract results
        output = []
        for res in results:
            body = res.get("body") or res.get("snippet") or ""
            if body:
                output.append(body)

        return "\n".join(output) if output else "No body content found in results."

    except Exception as e:
        return f"Error: DuckDuckGo search failed due to: {str(e)}"
