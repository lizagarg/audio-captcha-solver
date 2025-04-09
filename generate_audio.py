import pyttsx3

text = "three seven one five"
engine = pyttsx3.init()

# Directly save as WAV (no mp3, no ffmpeg, no conversion)
engine.save_to_file(text, 'captchas/test1.wav')
engine.runAndWait()

print("✅ Audio file saved as test1.wav in captchas folder.")
