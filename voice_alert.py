import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """
    Speaks the given text using system voice.
    Example: speak("Scatter detected. Stopping spin.")
    """
    engine.say(text)
    engine.runAndWait()

# Optional: test run
if __name__ == "__main__":
    speak("Professor Johnny activated. System is online.")
    speak("Scatter detected. Stopping spin.")
    speak("Bet increased to 2.0.")
    speak("Bet decreased to 1.0.")

