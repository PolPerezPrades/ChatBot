import ollama
import tempfile

MODEL_NAME = "gemma3:4b"

client = ollama.Client()

def get_response(messages:dict["role":str, "content":str, "images":list]) -> str:
    stream = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )
    return stream

def get_paths(files:list) -> str:
    paths = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{file.name}") as tmp:
            tmp.write(file.read())
            temp_path = tmp.name
        paths.append(temp_path)
    return paths