import faiss
import numpy as np
from .embeddings import get_embedding

index = faiss.IndexFlatL2(384)
texts = []

def add_documents(docs):
    global texts
    embeddings = [get_embedding(d) for d in docs]
    index.add(np.array(embeddings))
    texts.extend(docs)

def search(query, k=3):
    q_emb = get_embedding(query)
    D, I = index.search(np.array([q_emb]), k)

    results = [texts[i] for i in I[0] if i < len(texts)]
    return results