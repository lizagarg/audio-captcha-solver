# 🎧 Audio CAPTCHA Solver

A Python project to decode audio CAPTCHAs, designed with accessibility in mind — especially for visually impaired users.

## 💡 Features
- Converts speech CAPTCHA to text
- Noise reduction support
- Uses Google Speech Recognition
- Easy audio generation with `pyttsx3`

## 🧠 Tech Stack
- Python 3.x
- SpeechRecognition
- Pyttsx3
- Noisereduce (optional for denoising)
- VS Code + GitHub

## 🚀 Run It
```bash
# Setup environment (if needed)
pip install -r requirements.txt

# Generate audio
python generate_audio.py

# Solve audio CAPTCHA
python decoder.py
