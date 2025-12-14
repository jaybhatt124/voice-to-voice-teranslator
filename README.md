# voice-to-voice-teranslator

A Python-based Voice-to-Voice Translator that converts spoken language into another language and plays it back as natural-sounding speech.
This project combines speech recognition, language translation, and AI voice synthesis into a single interactive application.

Features
Voice input via microphone or audio file
Accurate speech-to-text using AssemblyAI
Language translation using Python libraries
Natural AI voice output using ElevenLabs
Simple and interactive Gradio web interface
Clean file handling with pathlib and uuid

How It Works

Voice → Speech-to-Text → Translate → Text-to-Speech → Voice

User provides voice input
AssemblyAI converts speech into text
Text is translated into the target language
ElevenLabs generates AI voice from translated text
Output audio is played in the Gradio interface

Tech Stack
Python
Gradio
AssemblyAI API
ElevenLabs API
pathlib
uuid

Getting Started
Prerequisites
Python 3.8+
AssemblyAI API Key
ElevenLabs API Key

All requirements are in requirements.txt file

api key of elevenlabs and assembly ai is find at their official websites
https://elevenlabs.io/
https://www.assemblyai.com/

install all library of requirenments.txt AS:

python -m pip install reqirements.txt
or
pip install requirements.txt 
