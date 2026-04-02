import streamlit as st
from deep_translator import GoogleTranslator

# Set up the page
st.set_page_config(page_title="AI Mini-Translator", page_icon="🌍")

st.title("🌍 AI Mini-Translator")
st.markdown("Translate text between languages instantly using Google Translate technology.")

# Language selection
# We'll create a dictionary of some popular languages
languages_dict = {
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Yoruba': 'yo',
    'Igbo': 'ig',
    'Hausa': 'ha',
    'Arabic': 'ar',
    'Chinese': 'zh-CN',
    'Portuguese': 'pt'
}

# Create two columns for language selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From (Source Language)", options=list(languages_dict.keys()), index=0)

with col2:
    target_lang = st.selectbox("To (Target Language)", options=list(languages_dict.keys()), index=1)

# Text input
text_to_translate = st.text_area("Enter text to translate:", height=150, placeholder="Type something here...")

# Translation logic
if st.button("Translate Now"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text first!")
    else:
        try:
            # Initialize the translator
            translator = GoogleTranslator(source=languages_dict[source_lang], target=languages_dict[target_lang])
            
            # Perform translation
            translation = translator.translate(text_to_translate)
            
            # Display results
            st.markdown("---")
            st.subheader("Result:")
            st.success(translation)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Deep-Translator")
