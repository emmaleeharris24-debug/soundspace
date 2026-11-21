
import streamlit as st

st.set_page_config(
    page_title="SoundSpace",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 SoundSpace")

st.subheader("Your new home for music discovery.")

st.write(
    "Discover artists. Explore genres. Find your sound."
)

st.divider()

st.header("Let's get to know your music taste.")

favorite_artist = st.text_input(
    "Who's your favorite music artist?"
)

favorite_genre = st.selectbox(
    "What's your favorite genre?",
    ["R&B", "Hip-Hop", "Soul", "Jazz", "Pop", "Other"]
)

if st.button("Find My Sound"):
    if favorite_artist:
        st.success(
            f"Great choice! Let's explore more {favorite_genre} "
            f"music and artists like {favorite_artist}."
        )
    else:
        st.warning("Please enter your favorite artist first.")
