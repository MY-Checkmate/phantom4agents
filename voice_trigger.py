import pyttsx3
import speech_recognition as sr
import subprocess

engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()

def speak(text):
    print(f"[🎙️ SPEAKING]: {text}")
    engine.say(text)
    engine.runAndWait()

def run_command(cmd):
    try:
        subprocess.Popen(cmd, shell=True)
        speak("Report triggered.")
    except Exception as e:
        speak("Error running the command.")

print("🎤 Voice trigger active... say something!\n")

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"[🎧 Heard]: {command}")

            if "generate report" in command:
                run_command("python pdf_report.py")
            elif "status" in command:
                speak("System active and monitoring.")
            elif "threat alert" in command:
                speak("445 port open. Exploit active. Possible malware.")
            elif "stop listening" in command:
                speak("Voice system going offline.")
                break
        except sr.UnknownValueError:
            print("🤖 Sorry, couldn't understand that.")
        except Exception as e:
            print(f"Error: {e}")
