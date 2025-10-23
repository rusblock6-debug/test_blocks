import os
import json
import requests

DOCS_DIR = "docs"
OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL_NAME = "llama3.1:8b"

def combine_folder_text(folder_path):
    texts = []
    for root, _, files in os.walk(folder_path):
        for file in sorted(files):
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, encoding="utf-8") as f:
                    texts.append(f"\n### {file}\n" + f.read())
    return "\n\n".join(texts)

def generate_embedding(name, text):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": text
    })
    if response.status_code == 200:
        embedding = response.json()["embedding"]
        out_file = os.path.join(DOCS_DIR, f"{name}_combined.embeddings.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump({
                "source": name,
                "length": len(text),
                "embedding": embedding
            }, f, ensure_ascii=False, indent=2)
        print(f"✅ {name} — готово")
    else:
        print(f"⚠️ Ошибка для {name}: {response.status_code}")

def main():
    for folder in os.listdir(DOCS_DIR):
        full_path = os.path.join(DOCS_DIR, folder)
        if os.path.isdir(full_path):
            text = combine_folder_text(full_path)
            generate_embedding(folder, text)

if __name__ == "__main__":
    main()
