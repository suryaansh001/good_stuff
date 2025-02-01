import pyaudio
import wave
from pydub import AudioSegment

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"
MP3_OUTPUT_FILENAME = "voice.mp3"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("Recording...")

frames = []

try:
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
except KeyboardInterrupt:
    print("Recording stopped.")

# Stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Convert WAV to MP3
audio_segment = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
audio_segment.export(MP3_OUTPUT_FILENAME, format="mp3")
print(f"Saved as {MP3_OUTPUT_FILENAME}")