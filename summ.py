import speech_recognition as sr
from pydub import AudioSegment
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def transcribe_audio(file_path):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(file_path)
    audio.export("temp.wav", format="wav")

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

def extract_tasks(text):
    doc = nlp(text)
    tasks = []
    for sent in doc.sents:
        if "task" in sent.text.lower() or "remind" in sent.text.lower()or "do" in sent.text.lower():
            tasks.append(sent.text)
    return tasks

if __name__ == "__main__":
    mp3_file = "voice.mp3"
    text = transcribe_audio(mp3_file)
    print("Transcribed Text:")
    print(text)
    
    tasks = extract_tasks(text)
    print("\nExtracted Tasks:")
    for task in tasks:
        print(task)