import chromadb #one of the best vector database which is open source
from sentence_transformers import SentenceTransformer #best embedding model
from utils.logger import log_execution

#chromadb client initiasted and embedding model loaded
client = chromadb.PersistentClient(path="./db")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

#function descriptions
FUNCTION_METADATA = {
    "open_chrome": "Launches Chrome browser and opens Google.com",
    "open_calculator": "Opens the system calculator",
    "open_notepad": "Opens the system notepad or text editor",
    "open_spotify": "Opens Spotify music on the browser",
    "open_yt": "Opens YouTube player on the browser",
    "get_cpu_usage": "Retrieves CPU usage in percentage",
    "get_ram_usage": "Retrieves RAM usage in percentage",
    "execute_command": "Executes a shell command and returns output",
    "create_file": "Creates an empty file in the system",
    "delete_file": "Deletes a specific file in the system",
    "move_file": "Moves a file from source to destination"
}

#chromadb collection created to store function metadata
collection = client.get_or_create_collection(name="functions")

#adding function metadata to the collection
for func, description in FUNCTION_METADATA.items():
    collection.add(
        ids=[func],
        embeddings=[embedding_model.encode(description).tolist()]
    )

log_execution("ChromaDB Initialization", "SUCCESS", "Function metadata stored in ChromaDB.")

#retrieves the function name based on the user prompt, RAG defined!
def retrieve_function(user_prompt):
    try:
        query_embedding = embedding_model.encode(user_prompt).tolist()
        results = collection.query(query_embeddings=[query_embedding], n_results=1)

        if results["ids"] and results["ids"][0]:
            function_name = results["ids"][0][0]
            log_execution("Function Retrieval", "SUCCESS", f"Retrieved function: {function_name} for prompt: {user_prompt}")
            return {"function": function_name}

        log_execution("Function Retrieval", "WARNING", f"No matching function found for prompt: {user_prompt}")
        return {"error": "No matching function"}

    except Exception as e:
        log_execution("Function Retrieval", "ERROR", str(e))
        return {"error": f"Failed to retrieve function: {str(e)}"}
