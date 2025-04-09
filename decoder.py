import os
import speech_recognition as sr

# Folder containing audio CAPTCHAs (only .wav files)
captcha_folder = "captchas"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Initialize recognizer
recognizer = sr.Recognizer()

# Loop through each .wav file in the captchas folder
for filename in os.listdir(captcha_folder):
    if filename.endswith(".wav"):
        file_path = os.path.join(captcha_folder, filename)
        print(f"\n🔊 Processing {filename}...")

        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)

            try:
                # Recognize speech using Google Web Speech API
                decoded_text = recognizer.recognize_google(audio_data)
                print(f"✅ Decoded Text: {decoded_text}")

                # Save result to output folder
                with open(os.path.join(output_folder, filename + ".txt"), "w") as f:
                    f.write(decoded_text)

            except sr.UnknownValueError:
                print("❌ Could not understand the audio.")
            except sr.RequestError as e:
                print(f"⚠️ Could not request results; {e}")
