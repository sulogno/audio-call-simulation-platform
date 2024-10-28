# Audio Call Simulation Platform

A Python-based audio call simulation platform with real-time transcription and post-call playback, designed to mimic automated call handling workflows.

## Features

- **Caller ID Selection**: Allows selection of a contact to simulate the recipient's caller ID.
- **Automated Call Initiation**: Automatically initiates a call simulation to the chosen contact.
- **Real-Time Voice Transcription**: Records audio and transcribes the conversation in real time, with timeout management for a smooth experience.
- **Saved Transcripts**: Transcriptions are saved in the `transcripts` folder, with each file containing a date and time stamp.
- **Post-Call Playback**: Transcribed text is converted to speech for post-call audio review.

## Project Structure

- **audio/**: Stores audio files used in the project.
- **contacts/**: Contains `contacts.json`, a list of contacts used for caller ID selection.
- **scripts/**: Contains the main Python scripts for each functionality:
  - `select_caller.py`: Handles contact selection.
  - `initiate_call.py`: Simulates call initiation.
  - `record_and_transcribe.py`: Records and transcribes audio in real-time.
  - `text_to_speech.py`: Converts transcriptions to audio.
- **transcripts/**: Stores saved transcriptions with date and time.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sulogno/audio-call-simulation-platform.git
   cd audio-call-simulation-platform

## Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`





## Install Dependencies:

pip install -r requirements.txt


## Run the Main Workflow:

To initiate the full simulation, run:


python scripts/main_workflow.py



## requirements
Python 3.7+
Libraries: speech_recognition, gTTS, pyaudio
Future Improvements
Integrate with Skype API or VoIP platforms for real-time call handling.
Add a GUI for easier interaction and visualization.
