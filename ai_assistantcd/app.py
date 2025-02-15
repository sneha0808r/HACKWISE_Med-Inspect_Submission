import streamlit as st
import requests
import speech_recognition as sr
from voice_assistant import play_audio

st.set_page_config(page_title="एआई असिस्टेंट", layout="wide")

# 🎨 Home Page Design
st.title("🤖 हिंदी एआई असिस्टेंट")
st.write("नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ?")

# *ONDC Website & YouTube Help Link*
ONDC_WEBSITE = "https://ondc.org/"  # Official ONDC Website
ONDC_YOUTUBE_LINK = "https://youtu.be/V35MGlOVR7Y?si=On0d9yAtykJvJuyA"  # YouTube tutorial for ONDC

# Speech Recognition Function
def recognize_speech():
    recognizer = sr.Recognizer()

    # *Check if Microphone is Available*
    mic_list = sr.Microphone.list_microphone_names()
    if not mic_list:
        st.write("❌ माइक्रोफ़ोन उपलब्ध नहीं है। कृपया जांचें कि आपका माइक्रोफोन कनेक्टेड और अनुमति प्राप्त है।")
        return ""

    with sr.Microphone() as source:
        st.write("🎙 कृपया बोलें...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="hi-IN")
            st.write(f"🗣 आपने कहा: {command}")
            return command.lower()
        except sr.UnknownValueError:
            st.write("❌ मैं आपकी आवाज़ नहीं समझ पाया। कृपया फिर से कोशिश करें।")
            return ""
        except sr.RequestError:
            st.write("❌ आवाज प्रोसेसिंग में समस्या आई। कृपया इंटरनेट कनेक्शन जांचें।")
            return ""

# Store voice command globally
if "voice_command" not in st.session_state:
    st.session_state.voice_command = ""

# Create Buttons with Icons
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🎤 वॉइस असिस्टेंट"):
        play_audio("welcome_hi.mp3")

with col2:
    if st.button("💰 बैंकिंग सहायता"):
        play_audio("banking_hi.mp3")
        requests.get("http://127.0.0.1:5000/open_youtube?category=banking")

with col3:
    if st.button("🏢 छोटे व्यवसाय (ONDC)"):
        play_audio("ondc_hi.mp3")  # AI voice for ONDC
        requests.get(ONDC_WEBSITE)  # Open ONDC website

with col4:
    if st.button("📺 शिक्षा (YouTube)"):
        play_audio("education_hi.mp3")
        requests.get("https://youtu.be/YOUR_EDUCATION_VIDEO_LINK")  # Provide education YouTube link

with col5:
    st.button("🏥 स्वास्थ्य")  # Just an icon, non-functional

st.write("---")

# 🎙 Voice Command Actions
st.header("🎙 वॉइस कमांड सहायता")

# Text Input + Voice Command Button
col1, col2 = st.columns(2)

with col1:
    text_input = st.text_input("आप क्या पूछना चाहते हैं? (हिंदी में लिखें)", value=st.session_state.voice_command)

with col2:
    if st.button("🎤 वॉइस इनपुट"):
        voice_command = recognize_speech()  # Captures user's voice immediately
        if voice_command.startswith("❌"):
            st.write(voice_command)  # Show error message
        else:
            st.session_state.voice_command = voice_command  # Update session state
            text_input = voice_command  # Update text field

            # *Process Speech Input Immediately*
            if "कृषि" in voice_command:
                play_audio("youtube_learning_hi.mp3")
                requests.get("http://127.0.0.1:5000/open_youtube?category=education")

            elif "बैंक" in voice_command:
                play_audio("banking_hi.mp3")
                requests.get("http://127.0.0.1:5000/open_youtube?category=banking")

            elif "कुलदीप को कॉल करें" in voice_command:
                play_audio("call_kuldeep_hi.mp3")
                requests.get("http://127.0.0.1:5000/call_kuldeep")

            elif "छोटा व्यवसाय" in voice_command or "बिजनेस शुरू करना" in voice_command or "व्यापार" in voice_command:
                play_audio("ondc_hi.mp3")  # AI voice for ONDC
                requests.get(ONDC_WEBSITE)  # Open ONDC website
                st.write("✅ यदि आपको ONDC का उपयोग समझना है, तो कृपया यूट्यूब वीडियो देखें।")
                play_audio("ondc_yt_hi.mp3")  # AI voice suggesting YouTube help

            else:
                play_audio("unknown_command_hi.mp3")
                st.write("❌ क्षमा करें, मैं इसे समझ नहीं पाया।")

# *Process Text Input When Button is Clicked*
if st.button("🔍 जवाब प्राप्त करें"):
    user_input = text_input.lower()  # Convert to lowercase

    if "कृषि" in user_input:
        play_audio("youtube_learning_hi.mp3")
        requests.get("http://127.0.0.1:5000/open_youtube?category=education")

    elif "बैंक" in user_input:
        play_audio("banking_hi.mp3")
        requests.get("http://127.0.0.1:5000/open_youtube?category=banking")

    elif "कुलदीप को कॉल करें" in user_input:
        play_audio("call_kuldeep_hi.mp3")
        requests.get("http://127.0.0.1:5000/call_kuldeep")

    elif "छोटा व्यवसाय" in user_input or "बिजनेस शुरू करना" in user_input or "व्यापार" in user_input:
        play_audio("ondc_hi.mp3")  # AI voice for ONDC
        requests.get(ONDC_WEBSITE)  # Open ONDC website
        st.write("✅ यदि आपको ONDC का उपयोग समझना है, तो कृपया यूट्यूब वीडियो देखें।")
        play_audio("ondc_yt_hi.mp3")  # AI voice suggesting YouTube help

    else:
        play_audio("unknown_command_hi.mp3")
        st.write("❌ क्षमा करें, मैं इसे समझ नहीं पाया।")