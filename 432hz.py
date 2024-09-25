import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment

# 1. Generate a 432Hz sine wave
def generate_432hz_tone(duration_seconds, sample_rate=44100):
    frequency = 432  # Frequency of the tone (432 Hz)
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave (amplitude = 0.5)
    return tone

# 2. Save the generated tone as a WAV file
def save_wav(filename, tone, sample_rate=44100):
    # Normalize the tone to the range of int16
    tone = np.int16(tone * 32767)
    write(filename, sample_rate, tone)

# 3. Convert WAV to MP3 using pydub
def convert_to_mp3(wav_filename, mp3_filename):
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")

# 4. Generate and save the 432Hz tone for 5 minutes (300 seconds)
duration_seconds = 300  # 5 minutes
sample_rate = 44100  # Standard sample rate for audio files

# Generate the tone
tone = generate_432hz_tone(duration_seconds, sample_rate)

# Save as WAV
wav_filename = "432hz_tone.wav"
save_wav(wav_filename, tone, sample_rate)

# Convert to MP3
mp3_filename = "432hz_tone.mp3"
convert_to_mp3(wav_filename, mp3_filename)

print("MP3 file created:", mp3_filename)

