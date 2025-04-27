import streamlit as st
import random
import pandas as pd
from datetime import datetime

# --- Custom CSS for a fresh look ---
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(120deg, #f8fafc, #e0c3fc);
        padding: 24px;
        border-radius: 14px;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(120deg, #f9fbe7, #e0f7fa);
        padding: 24px;
        border-radius: 14px;
    }
    h1, h2, h3 {
        color: #3d155f;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stButton button {
        background: linear-gradient(120deg, #ff758c, #ff7eb3);
        color: #fff;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 17px;
        font-weight: 600;
    }
    .stButton button:hover {
        background: linear-gradient(120deg, #ff7eb3, #ff758c);
    }
    .stProgress > div > div > div {
        background: linear-gradient(120deg, #43cea2, #185a9d);
    }
    .stMarkdown {
        font-size: 17px;
        color: #3d155f;
    }
    .card {
        background: #fff;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 6px 16px rgba(61, 21, 95, 0.08);
        margin-bottom: 24px;
    }
    .profile-card {
        background: linear-gradient(120deg, #43cea2, #185a9d);
        color: #fff;
        padding: 24px;
        border-radius: 14px;
        text-align: center;
    }
    .badge-card {
        background: #fff;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 6px 16px rgba(61, 21, 95, 0.08);
        margin-bottom: 24px;
    }
    .badge {
        display: inline-block;
        background: #ff758c;
        color: #fff;
        padding: 7px 14px;
        border-radius: 22px;
        margin: 7px;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session State for Adventurers ---
if "adventurers" not in st.session_state:
    st.session_state.adventurers = {}

# --- App Banner and Title ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    try:
        st.image("./assets/logo.png", width=110)
    except Exception:
        st.write("🌱")
with col_title:
    st.markdown("<h1 style='color: #3d155f;'>🚀 Growth Quest</h1>", unsafe_allow_html=True)

# --- Daily Spark (Motivation) ---
st.markdown("<div class='card'><h2 style='color: #3d155f;'>✨ Inspiration for Today</h2>", unsafe_allow_html=True)
inspirations = [
    "Progress is progress, no matter how small.",
    "Every challenge is a new adventure.",
    "You are the author of your own story.",
    "Learning is a treasure that follows its owner everywhere.",
    "Mistakes are proof you are trying.",
    "Curiosity is the compass to discovery.",
    "Your journey is unique—embrace it!"
]
st.markdown(f"<h3 style='color: #ff758c;'>{random.choice(inspirations)}</h3>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Fun Fact Section ---
st.markdown("<div class='card'><h2 style='color: #3d155f;'>🎲 Random Fun Fact</h2>", unsafe_allow_html=True)
fun_facts = [
    "Did you know? Honey never spoils.",
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "The Eiffel Tower can be 15 cm taller during hot days."
]
st.markdown(f"<i>{random.choice(fun_facts)}</i>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Sidebar: Adventurer Info ---
st.sidebar.markdown("<h2 style='color: #3d155f;'>🧑‍🚀 Your Adventure Log</h2>", unsafe_allow_html=True)
alias = st.sidebar.text_input("What should we call you?")
quest = st.sidebar.text_input("What's your current mission?")
style_pref = st.sidebar.selectbox(
    "Pick your learning vibe:", ["Visual Explorer", "Wordsmith", "Hands-on Hero", "Audio Seeker"]
)
avatar = st.sidebar.file_uploader("Upload your avatar", type=["jpg", "jpeg", "png"])
about_you = st.sidebar.text_area("Share a fun fact about yourself")
passions = st.sidebar.text_input("What excites you? (e.g., robotics, painting, math)")
contact = st.sidebar.text_input("Contact (optional)")

if alias:
    if alias not in st.session_state.adventurers:
        st.session_state.adventurers[alias] = {
            "energy": 5,
            "wisdom": 5,
            "feedback": "",
            "milestones": [],
            "badges": [],
            "mood": "🙂",
            "weekly_journal": "",
            "avatar": None,
            "about_you": "",
            "passions": "",
            "contact": "",
        }

    # Update adventurer profile
    st.session_state.adventurers[alias]["avatar"] = avatar
    st.session_state.adventurers[alias]["about_you"] = about_you
    st.session_state.adventurers[alias]["passions"] = passions
    st.session_state.adventurers[alias]["contact"] = contact

    # --- Mood Tracker (moved up) ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>🌈 How's Your Spirit?</h2>", unsafe_allow_html=True)
    mood_options = [
        "🙂 Content", "😃 Pumped", "🤔 Curious", "😴 Tired", "😅 Stressed", "😇 Grateful", "😎 Confident"
    ]
    spirit = st.radio("Choose your vibe:", mood_options, horizontal=True)
    st.session_state.adventurers[alias]["mood"] = spirit
    st.markdown(f"<h3 style='color: #43cea2;'>Today's mood: {spirit}</h3></div>", unsafe_allow_html=True)

    # --- Profile Card (after mood) ---
    st.markdown("<div class='profile-card'><h2 style='color: white;'>🧑‍🚀 Adventurer Profile</h2>", unsafe_allow_html=True)
    if st.session_state.adventurers[alias]["avatar"] is not None:
        st.image(st.session_state.adventurers[alias]["avatar"], width=110)
    st.markdown(f"<h3 style='color: white;'>Welcome, {alias}!</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Mission: <i>{quest}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Learning Vibe: <i>{style_pref}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>About: <i>{about_you}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Passions: <i>{passions}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Contact: <i>{contact}</i></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Progress Tracker ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>📊 Your Progress Meter</h2>", unsafe_allow_html=True)
    col_energy, col_wisdom = st.columns(2)
    with col_energy:
        st.session_state.adventurers[alias]["energy"] = st.slider(
            "How energized are you? (1-10)", 1, 10, st.session_state.adventurers[alias]["energy"]
        )
    with col_wisdom:
        st.session_state.adventurers[alias]["wisdom"] = st.slider(
            "How much have you learned? (1-10)", 1, 10, st.session_state.adventurers[alias]["wisdom"]
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Weekly Journal ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>📝 Weekly Journal</h2>", unsafe_allow_html=True)
    st.session_state.adventurers[alias]["weekly_journal"] = st.text_area(
        "Reflect on your week: What did you discover? What will you try next?",
        value=st.session_state.adventurers[alias]["weekly_journal"]
    )
    if st.button("Save Journal"):
        st.success("Journal entry saved! Keep exploring! 🚀")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Learning Tips (with extra tips) ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>🧭 Explorer's Toolkit</h2>", unsafe_allow_html=True)
    explorer_tips = {
        "Visual Explorer": [
            "Sketch your ideas and concepts.",
            "Use color-coded sticky notes.",
            "Try infographics and visual summaries.",
            "Create digital collages for inspiration."
        ],
        "Wordsmith": [
            "Write a daily learning log.",
            "Summarize what you read in your own words.",
            "Make crossword puzzles with key terms.",
            "Draft a letter explaining a concept to a friend."
        ],
        "Hands-on Hero": [
            "Build a model or prototype.",
            "Teach someone else what you learned.",
            "Join a hackathon or maker event.",
            "Document your process with photos."
        ],
        "Audio Seeker": [
            "Record your own audio notes.",
            "Make playlists of educational podcasts.",
            "Try voice-to-text for brainstorming.",
            "Discuss topics in a study group call."
        ],
    }
    st.markdown(f"<h3 style='color: #ff758c;'>Tips for {style_pref}s:</h3>", unsafe_allow_html=True)
    for tip in explorer_tips[style_pref]:
        st.markdown(f"- {tip}")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Leaderboard (Top Adventurers) ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>🏅 Adventurer Leaderboard</h2>", unsafe_allow_html=True)
    leaderboard = []
    for adventurer, stats in st.session_state.adventurers.items():
        leaderboard.append({
            "Alias": adventurer,
            "Energy": stats["energy"],
            "Wisdom": stats["wisdom"],
            "Mood": stats["mood"],
        })
    if leaderboard:
        df = pd.DataFrame(leaderboard)
        df = df.sort_values(by=["Energy", "Wisdom"], ascending=False)
        st.table(df)
    else:
        st.write("No adventurers yet.")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Progress Chart ---
    st.markdown("<div class='card'><h2 style='color: #3d155f;'>📈 Progress Over Time</h2>", unsafe_allow_html=True)
    if leaderboard:
        st.line_chart(df.set_index("Alias")[["Energy", "Wisdom"]])
    else:
        st.write("No data to chart yet.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Signature ---
st.markdown(
    "<div style='text-align:center; margin-top:40px; font-size:22px; color:#ff758c;'>"
    "❤️ Made with love by <b>Ahmer Abbasi</b> ❤️"
    "</div>",
    unsafe_allow_html=True
)