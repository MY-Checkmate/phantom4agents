import speech_recognition as sr
import pyttsx3
import subprocess
import yaml

# Initialize speech engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()

def speak(text):
    """Speak the given text."""
    print(f"[🎙️ SPEAKING]: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a voice command."""
    with mic as source:
        print("\n🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

def load_commands():
    """Load voice commands from config.yaml."""
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config.get("voice_commands", [])

def process_command(command, commands):
    """Process the given voice command."""
    for cmd in commands:
        if cmd["trigger"] in command:
            speak(f"Executing: {cmd['description']}")
            if cmd["action"] == "exit":
                return False
            subprocess.Popen(cmd["action"], shell=True)
            return True
    speak("Command not recognized.")
    return True

if __name__ == "__main__":
    speak("Voice Cortex online. Awaiting commands.")
    commands = load_commands()
    while True:
        cmd = listen()
        if not cmd:
            continue
        if not process_command(cmd, commands):
            break
