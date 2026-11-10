from ddgs import DDGS

def search_web(query: str, limit: int = 5):
    with DDGS() as search:
        results = search.text(query, max_results=limit)
        return [
            {
                "title": item.get("title"),
                "url": item.get("href"),
                "snippet": item.get("body"),
            }
            for item in results
        ]