# good_stuff
Real-Time Conversation Summarizer

This project records and transcribes live audio using OpenAI Whisper and extracts key points and task assignments using GPT-4.

Features

Real-time voice transcription using Whisper.

Automatic conversation summarization with OpenAI.

Task extraction from conversations.

Setup

Install dependencies:

pip install openai whisper pyaudio wave python-dotenv

Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

Run the script:

python main.py

Notes

Interrupt with Ctrl + C to stop recording.

Summaries and tasks will be displayed after transcription.

🚀 Currently in development!

