import streamlit as st
from deep_translator import GoogleTranslator

# 1. Setup the Page
st.set_page_config(page_title="Boss-Level English Academy", page_icon="🎓")

st.title("🎓 Saurav's Boss-Level English Academy")
st.write("Welcome, Intern. Try not to fail the class today.")

st.divider()

# 2. The Real Translator (Turkish/German to English)
st.header("🌍 The Real Translator")
st.write("Type your Turkish or German here, and let the algorithm do the heavy lifting.")

lang_choice = st.radio("Translate from:", ("Turkish", "German"))
text_to_translate = st.text_area("Enter text to translate:")

if st.button("Translate to English"):
    if text_to_translate:
        source_lang = "tr" if lang_choice == "Turkish" else "de"
        translated = GoogleTranslator(source=source_lang, target='en').translate(text_to_translate)
        st.success(f"**Perfect English:** {translated}")
    else:
        st.warning("You have to actually type something first, Boss.")

st.divider()

# 3. The Joke Feature: The PUBG Translator
st.header("🎮 The PUBG Translator")
st.write("What you say in the lobby vs. what it actually means.")

pubg_phrases = {
    "I need help": "Please carry me, my brain is still lagging from the shisha bar.",
    "Let's push the enemy": "I am going to rush in blindly and get knocked immediately.",
    "Good game": "I literally did nothing, but thanks for the chicken dinner anyway."
}

phrase_choice = st.selectbox("Choose a gamer phrase:", list(pubg_phrases.keys()))

if st.button("Decode Gamer Talk"):
    st.info(f"**What she actually means:** {pubg_phrases[phrase_choice]}")