import faiss
import numpy as np

# Embedding dimension
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Store candidate names
candidate_store = []

def add_embeddings(vectors, candidate_names):

    global candidate_store

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)

    candidate_store.extend(candidate_names)

def search_embeddings(query_vector, top_k=5):

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(candidate_store):

            results.append({
                "candidate": candidate_store[idx],
                "distance": float(
                    distances[0][
                        list(indices[0]).index(idx)
                    ]
                )
            })

    return results