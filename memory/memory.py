import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os
import uuid

# Load .env
load_dotenv()

# OpenAI API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# NEW: Create default Chroma client
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
collection = chroma_client.get_or_create_collection("echo_memory")
# Function to embed text using OpenAI
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Store a new memory in ChromaDB
def store_interaction(user_input, echo_reply):
    combined = f"User: {user_input}\nEcho: {echo_reply}"
    embedding = get_embedding(combined)
    doc_id = str(uuid.uuid4())

    collection.add(
        documents=[combined],
        embeddings=[embedding],
        ids=[doc_id]
    )

# Search past memories based on semantic similarity
def search_memory(query, n_results=3):
    embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []
