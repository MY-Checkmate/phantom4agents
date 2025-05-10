import speech_recognition as sr
import pyttsx3
import subprocess

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

def speak(msg):
    print(f"[🧠] {msg}")
    engine.say(msg)
    engine.runAndWait()

def listen():
    with mic as source:
        print("\n🎙 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        speak("Couldn't understand.")
        return ""

def act(cmd):
    if "scan" in cmd:
        subprocess.Popen(["python", "sentinel_agent.py"])
        speak("Running scan.")
    elif "alert" in cmd:
        subprocess.Popen(["python", "alert_engine.py"])
        speak("Alert engine activated.")
    elif "memory" in cmd or "brain" in cmd:
        subprocess.Popen(["python", "chroma_brain.py"])
        speak("Memory brain online.")
    elif "stop" in cmd or "exit" in cmd:
        speak("Voice loop exiting.")
        return False
    else:
        speak("Unknown command.")
    return True

if __name__ == "__main__":
    speak("Voice loop online.")
    while True:
        cmd = listen()
        if not act(cmd): break
