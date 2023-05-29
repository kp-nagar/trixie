import vosk
import sys
import os
import pyaudio

# Define the Vosk model and the path to the model file
model = vosk.Model("model")

# Set up the microphone input
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

# Create a Vosk recognizer using the model
rec = vosk.KaldiRecognizer(model, 16000)

# Main program loop
while True:
    # Read audio data from the microphone
    data = stream.read(4000)
    
    # Process the audio data
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)
    else:
        rec.PartialResult()

# Print the final result
result = rec.FinalResult()
print(result)

# Clean up resources
stream.stop_stream()
stream.close()
audio.terminate()
