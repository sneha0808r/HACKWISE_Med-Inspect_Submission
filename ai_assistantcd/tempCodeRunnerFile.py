import os
import playsound

def play_audio(file_name):
    """Hindi pre-recorded audio play करता है।"""
    file_path = os.path.join("voice_clips", file_name)
    if os.path.exists(file_path):
        playsound.playsound(file_path)
    else:
        print(f"ऑडियो फ़ाइल {file_name} नहीं मिली!")

# Example Usage
play_audio("welcome_hi.mp3")  # स्वागत संदेश