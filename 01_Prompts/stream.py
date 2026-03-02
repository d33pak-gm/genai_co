import ollama

model = "llama3.1:latest"

def stream_response(prompt: str):
    stream = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print()  # newline at end

stream_response("Explain transformers architecture in detail")