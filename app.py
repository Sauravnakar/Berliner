import streamlit as st
import random
from deep_translator import GoogleTranslator

# 1. Setup the Page
st.set_page_config(page_title="English Voice Coach", page_icon="🎙️", layout="centered")

# 2. Interactive Memory 
if 'current_task' not in st.session_state:
    st.session_state.current_task = None

# 3. The Speaking Tasks Database (With German translations and Cheat Sheets)
tasks = [
    {
        "topic_en": "Describe your absolute favorite food.",
        "topic_de": "Beschreibe dein absolutes Lieblingsessen.",
        "hints": "lecker (delicious), scharf (spicy), süß (sweet), kochen (to cook), Zutaten (ingredients)"
    },
    {
        "topic_en": "Tell me about a movie or series you really love.",
        "topic_de": "Erzähl mir von einem Film oder einer Serie, die du wirklich liebst.",
        "hints": "Handlung (plot), lustig (funny), spannend (exciting), Schauspieler (actor), Staffel (season)"
    },
    {
        "topic_en": "What is the most annoying thing about playing PUBG?",
        "topic_de": "Was ist das Nervigste am PUBG spielen?",
        "hints": "Verbindung (connection), abstürzen (to crash), verstecken (to hide), laut (loud), verlieren (to lose)"
    },
    {
        "topic_en": "Describe what your perfect weekend looks like.",
        "topic_de": "Beschreibe, wie dein perfektes Wochenende aussieht.",
        "hints": "ausschlafen (to sleep in), entspannen (to relax), spazieren gehen (to go for a walk), treffen (to meet)"
    }
]

# 4. The UI Engine
st.title("🎙️ The Voice Note Coach")
st.write("No more being shy. This is your safe space to practice speaking English. Take your time, build your sentence, and hit record.")
st.divider()

# Button to get a new task
if st.button("🎯 Give Me a Speaking Task", use_container_width=True):
    st.session_state.current_task = random.choice(tasks)

# 5. Display the Task and Cheat Sheet
if st.session_state.current_task:
    task = st.session_state.current_task
    
    st.header("Your Task:")
    st.success(f"**{task['topic_en']}**")
    st.caption(f"*(German: {task['topic_de']})*")
    
    st.write("---")
    st.subheader("📝 Vocabulary Cheat Sheet")
    st.write("Here are some words you might need for this topic:")
    st.info(task['hints'])
    
    st.warning("📱 **Action:** Use these words to record a short English voice note and send it to me. Don't worry about grammar, just speak!")

st.divider()

# 6. The SOS Translator
st.subheader("🆘 SOS Dictionary")
st.write("Stuck on a specific German word while recording? Type it here to get the English word instantly.")

col1, col2 = st.columns([3, 1])
with col1:
    german_word = st.text_input("German word:", label_visibility="collapsed", placeholder="Enter a word (e.g. anstrengend)")
with col2:
    translate_btn = st.button("Translate")

if translate_btn and german_word:
    english_translation = GoogleTranslator(source='de', target='en').translate(german_word)
    st.success(f"**English:** {english_translation}")
