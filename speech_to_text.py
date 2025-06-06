import speech_recognition as sr

def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Speak something... (Recording)")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
        audio = recognizer.listen(source)
        print("Processing your input...")

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(" You said: ", text)

        # Optional: Save to a text file
        with open("output.txt", "w") as f:
            f.write(text)

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f" Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
