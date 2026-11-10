from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer(
    "google/embeddinggemma-300m"
)

class Request(BaseModel):
    text: str

@app.post("/embed")
def embed(req: Request):
    vector = model.encode(req.text).tolist()

    return {
        "embedding": vector,
        "dimension": len(vector)
    }