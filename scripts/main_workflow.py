from select_caller import select_caller_id
from initiate_call import initiate_call
from record_and_transcribe import real_time_transcription
from text_to_speech import text_to_speech
import speech_recognition as sr
import os
from datetime import datetime

def main_workflow():
    # Step 1: Select Caller ID
    selected_contact = select_caller_id()
    
    # Step 2: Initiate Call
    initiate_call(selected_contact)
    
    # Step 3: Real-Time Transcription of Conversation
    transcription = real_time_transcription()
    
    # Step 4: Post-Call Text-to-Speech Playback
    text_to_speech(transcription)
def real_time_transcription():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Real-Time Transcription started. Speak now...")

    transcription = ""
    timeout_count = 0
    max_timeouts = 3  # Set a maximum number of timeouts before ending

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print("Transcription:", text)
                transcription += text + " "
                timeout_count = 0  # Reset timeout count when audio is detected
                
                # End the transcription if the user says a specific phrase, e.g., "stop transcription"
                if "stop transcription" in text.lower():
                    print("Stopping transcription...")
                    break

            except sr.UnknownValueError:
                print("Could not understand audio, please try again.")
            except sr.WaitTimeoutError:
                print("Listening timed out, waiting for speech...")
                timeout_count += 1
                if timeout_count >= max_timeouts:
                    print("Ending transcription due to inactivity.")
                    break
            except sr.RequestError:
                print("Error with the speech recognition service.")
            except KeyboardInterrupt:
                print("Manual interruption. Exiting...")
                break

    # Add date and time to transcription
    if transcription:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamped_transcription = f"Date and Time: {current_time}\n\n{transcription}"
        
        # Save the transcription to a text file in the transcripts folder
        filename = f"transcripts/transcription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(timestamped_transcription)
        
        print(f"Transcription saved with date and time as: {filename}")

    return transcription
if __name__ == "__main__":
    print("Starting the Skype Automation Simulation Workflow...")
    main_workflow()
