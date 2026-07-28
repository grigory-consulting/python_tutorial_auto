# Retrieval Augmented Generation (RAG) System 
# 

# Pipeline
# 1. chunk - split each .txt into ~1500 characters 
# 2. embed - one vector per chunk 
# 3. retrieve - embed the question, compare with embedding (cosine similarity) from the chunks. Take top 3 chunks.
# 4. generate - answer with a model, grounded in those chunks ONLY

from openai import OpenAI
from pathlib import Path 
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

CHAT_MODEL = "qwen3-0.6b"
EMBEDDING_MODEL = "text-embedding-nomic-embed-text-v1.5"
CHUNK_SIZE = 1500 # characters; roughly 350 tokens 
TOP_K = 3 # top 3 chunks for the model 

# Specification of embedding model: prefixes 
DOC_PREFIX = "search_document: "
QUERY_PREFIX = "search_query: "

QUESTION = "What does it mean that a vehicle satisfies a self-driving test?"
QUESTION = "What does SAE J3016 say?"

CORPUS_PATH = Path(__file__).resolve().parent / "wiki_corpus"

def chunk_file(path):
    chunks, current = [], "" # current is current chunk 

    for paragraph in path.read_text().split("\n\n"):
        if len(current) + len(paragraph) > CHUNK_SIZE and current:
            chunks.append(current.strip()) # strip removes leading and trailing whitespaces 
            current = ""
        current += paragraph + "\n\n"

    if current.strip(): # last chunk
        chunks.append(current.strip())
    return [{"file": path.name, "text": c} for c in chunks]
        
def embed(corpus):
    chunks = []
    for path in sorted(corpus.glob("*.txt")):
        chunks.extend(chunk_file(path))
    for start in range(0, len(chunks), 32): # batches of 32 chunks
        batch = chunks[start:start+32]
        result = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=[DOC_PREFIX + c["text"] for c in batch]
        )
        for chunk,data in zip(batch, result.data):
            chunk["vector"] = data.embedding

    return chunks

def cosine(a,b):
        import math
        dot = sum(x*y for x,y in zip(a,b)) # zip generates tuples
        return dot / (math.hypot(*a) * math.hypot(*b))


def retrieve(embeddings, question):
    question_vector = client.embeddings.create( model=EMBEDDING_MODEL, input=[QUERY_PREFIX+question]).data[0].embedding
    ranked = sorted(embeddings, key=lambda c: cosine(question_vector,c["vector"]), reverse=True)
    return ranked[:TOP_K]

def answer(question, corpus):
    embeddings = embed(corpus)
    hits = retrieve(embeddings,question)
    context = "\n\n---\n\n".join(f"[{h['file']}]\n{h['text']}" for h in hits)
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Answer using only the provided context. If the "
                        "context does not contain the answer, say so. /no_think"},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
        temperature=0.0,
        max_tokens=300,
    )
    print(f"\nretrieved: {', '.join(h['file'] for h in hits)}")
    print(f"\n{response.choices[0].message.content.strip()}")


answer(QUESTION,CORPUS_PATH)

