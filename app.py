import streamlit as st
import random

# 1. Setup the Page
st.set_page_config(page_title="The Daily Energy", page_icon="✨", layout="centered")

# 2. Interactive Memory 
if 'current_hype' not in st.session_state:
    st.session_state.current_hype = ""
if 'current_task' not in st.session_state:
    st.session_state.current_task = ""

# 3. The Content Databases 
# Real, genuine hype that makes her smile without being overly romantic.
hypes = [
    "You actually have really good energy. Don't let anyone ruin your vibe today.",
    "Your English is genuinely getting better every day. Stop doubting yourself.",
    "You are much smarter than you give yourself credit for. Trust your own brain.",
    "Take a deep breath. You are doing great, and whatever you are stressing about isn't that big of a deal.",
    "You have a great laugh. Make sure you find an excuse to use it today.",
    "You are a very resilient person. Keep your head up, Boss.",
    "Forget about the game for a second—you are just a genuinely cool person to talk to."
]

# Fun, real-world voice note tasks to build her English and keep the conversation going.
tasks = [
    "🎤 Send me a voice note in English telling me about a time you laughed so hard you couldn't breathe.",
    "🎤 Send me a voice note in English describing your absolute perfect weekend (no games allowed).",
    "🎤 Send me a voice note in English telling me one thing you are genuinely really proud of.",
    "🎤 Send me a voice note in English explaining your favorite movie and why I need to watch it.",
    "🎤 Send me a voice note in English telling me what your biggest goal for this year is."
]

# 4. The UI Engine
st.title("✨ The Daily Energy App")
st.write("Whenever you are bored, feeling shy, or just need a reset. Choose your button.")
st.divider()

# Button 1: The Good Energy
if st.button("🌟 Give Me Some Good Energy", use_container_width=True):
    st.session_state.current_hype = random.choice(hypes)
    st.session_state.current_task = ""

# Button 2: The Interactive English Task
st.write("---")
st.subheader("🗣️ The Confidence Challenge")
st.write("You want to stop being shy when you speak? Time to practice.")

if st.button("📩 Give Me an English Task", use_container_width=True):
    st.session_state.current_task = random.choice(tasks)
    st.session_state.current_hype = ""

# 5. Display the Results dynamically
if st.session_state.current_hype:
    st.success(f"**{st.session_state.current_hype}**")

if st.session_state.current_task:
    st.info(f"**{st.session_state.current_task}**")
    st.warning("⚠️ **Rule:** You MUST record a voice note in English and send it to me. No texting. Take your time, I won't judge your accent.")
