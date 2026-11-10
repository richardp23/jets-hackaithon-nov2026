import os
import requests
from fastapi import FastAPI
from web_search import search_web

app = FastAPI()

@app.get("/api/v1/search")
def search(query: str):
    results = search_web(query, limit=5)
    model = os.getenv("EMBEDDING_MODEL", "embeddinggemma")
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    emb = requests.post(
        f"{ollama_url}/api/embed",
        json={"model": model, "input": query},
        timeout=60
    )
    emb.raise_for_status()
    vector = emb.json()["embeddings"][0]

    return {
        "query": query,
        "results": results,
        "embedding_dimension": len(vector),
        "embedding_preview": vector[:10]
    }