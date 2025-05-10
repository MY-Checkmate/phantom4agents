import speech_recognition as sr
import subprocess
from chromadb import Client
from chromadb.utils import embedding_functions
import time

# Setup embedding + collection
client = Client()
embed = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="1manarmy_memory", embedding_function=embed)

# Voice recognition setup
r = sr.Recognizer()
mic = sr.Microphone()

def listen_command():
    with mic as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"[🗣️] You said: {command}")
        return command
    except Exception as e:
        print("[❌] Could not understand:", e)
        return None

def ask_brain(question):
    print("🧠 Asking 1manarmy...")
    results = collection.query(query_texts=[question], n_results=3)
    docs = results["documents"][0]
    context = "\n".join(docs)

    prompt = f"You are 1manarmy, an offline AI trained on tactical memory. Based on this:\n\n{context}\n\nQ: {question}\nA:"

    print("🤖 Thinking...")
    result = subprocess.run(["ollama", "run", "mistral"], input=prompt, text=True, capture_output=True)
    print("\n🧠 Response:\n", result.stdout)

# MAIN LOOP
if __name__ == "__main__":
    print("=== 1manarmy Voice Intelligence Mode ===")
    while True:
        cmd = listen_command()
        if cmd:
            if "exit" in cmd.lower():
                print("👋 Exiting.")
                break
            ask_brain(cmd)
        time.sleep(1)
