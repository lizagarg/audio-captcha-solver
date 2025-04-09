import os
import librosa
import noisereduce as nr
import speech_recognition as sr
import soundfile as sf

def reduce_noise(audio_path):
    y, sr_ = librosa.load(audio_path, sr=None)
    reduced = nr.reduce_noise(y=y, sr=sr_)
    
    cleaned_path = os.path.join("output", "cleaned.wav")
    sf.write(cleaned_path, reduced, sr_)
    return cleaned_path

def decode_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

if __name__ == "__main__":
    input_path = "captchas/test1.wav"
    cleaned_path = reduce_noise(input_path)
    result = decode_audio(cleaned_path)

    with open("output/test1.wav.txt", "w") as f:
        f.write(result)

    print("Decoded CAPTCHA:", result)
