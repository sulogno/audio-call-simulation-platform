from gtts import gTTS
import os

def text_to_speech(text):
    if not text:
        print("No transcription available for text-to-speech.")
        return
    
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("audio/post_call_summary.mp3")
    print("Text-to-speech conversion completed. Playing audio...")

    # Play the audio file
    os.system("start audio/post_call_summary.mp3")  # For Windows

if __name__ == "__main__":
    # Sample text for testing
    sample_text = "Hello, this is a test of the post-call text-to-speech conversion."
    text_to_speech(sample_text)
