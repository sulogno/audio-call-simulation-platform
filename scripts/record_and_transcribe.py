import speech_recognition as sr
import time

def real_time_transcription():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Real-Time Transcription started. Speak now...")

    transcription = ""
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print("Transcription:", text)
                transcription += text + " "
                
                # You can stop this loop with a specific command
                if "stop transcription" in text.lower():
                    print("Stopping transcription...")
                    break

            except sr.UnknownValueError:
                print("Could not understand audio, please try again.")
            except sr.RequestError:
                print("Error with the speech recognition service.")
            except KeyboardInterrupt:
                print("Manual interruption. Exiting...")
                break

    return transcription

if __name__ == "__main__":
    real_time_transcription()
