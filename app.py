import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="AI Voice Translator", page_icon="🌐")

st.title("🌐 AI Voice Translator")
st.write("Translate and hear the pronunciation instantly.")

# Language dictionary (Mapping for translator and gTTS)
languages_dict = {
    'English': 'en', 'French': 'fr', 'Spanish': 'es', 'German': 'de', 
    'Yoruba': 'yo', 'Igbo': 'ig', 'Hausa': 'ha', 'Arabic': 'ar', 
    'Chinese': 'zh-CN', 'Portuguese': 'pt', 'Russian': 'ru', 'Japanese': 'ja'
}

# Input Section
text_to_translate = st.text_area("What should I translate?", placeholder="Enter text here...", height=150)

# Target language selection
target_lang_name = st.selectbox("Translate to:", options=list(languages_dict.keys()), index=4)
target_lang_code = languages_dict[target_lang_name]

if st.button("✨ Magic Translate & Speak"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text first!")
    else:
        try:
            # 1. Translation
            translator = GoogleTranslator(source='auto', target=target_lang_code)
            translation = translator.translate(text_to_translate)
            
            st.markdown("---")
            st.subheader("Result:")
            st.success(translation)
            
            # 2. Text-to-Speech Logic
            # gTTS handles most languages, but we wrap it in a try-block just in case
            tts = gTTS(text=translation, lang=target_lang_code)
            tts.save("speech.mp3")
            
            # 3. Audio Player
            st.audio("speech.mp3", format="audio/mp3")
            
            # Clean up the file after playing (optional but good practice)
            os.remove("speech.mp3")
            
        except Exception as e:
            st.error(f"Error: {e}. Note: Some languages may not support voice yet.")

st.markdown("---")
st.info("Tip: After translating, press the 'Play' button on the audio bar to hear the pronunciation!")
