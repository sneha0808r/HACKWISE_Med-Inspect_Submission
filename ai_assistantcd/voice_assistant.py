import os
import playsound

def play_audio(file_name):
    """Plays pre-recorded Hindi AI voice responses using playsound."""
    
    # Ensure correct path to voice clips
    file_path = os.path.abspath(os.path.join("voice_clips", file_name))

    if os.path.exists(file_path):
        try:
            playsound.playsound(file_path, True)  # Blocking mode (ensures it plays fully)
        except Exception as e:
            print(f"❌ ऑडियो प्लेबैक में समस्या आई: {e}")
    else:
        print(f"❌ ऑडियो फ़ाइल {file_name} नहीं मिली!")

# Example Usage
if __name__ == "__main_r_":
    play_audio("welcome_hi.mp3")  # Test playback