
import streamlit as st

st.set_page_config(
    page_title="SoundSpace | Discover Your Sound",
    page_icon="🎵",
    layout="wide"
)

# SoundSpace curated music library


# SoundSpace curated music library


# SoundSpace curated music library

# Artists with similar sounds and musical styles

artist_connections = {
    "frank ocean": ["Blood Orange", "Sampha", "Dijon"],
    "mac miller": ["Isaiah Rashad", "Saba", "MAVI"],
    "sade": ["Cleo Sol", "Snoh Aalegra", "Goapele"],
    "dijon": ["Sampha", "Blood Orange", "Steve Lacy"],
    "sampha": ["Dijon", "Blood Orange", "Kelela"],
    "isaiah rashad": ["Mac Miller", "Saba", "MAVI"],
    "blood orange": ["Frank Ocean", "Dijon", "Sampha"],
    "chloe x halle": ["Kelela", "Ravyn Lenae", "Snoh Aalegra"],
    "aminé": ["Saba", "Mac Miller", "MAVI"],
    "snoh aalegra": ["Cleo Sol", "Sade", "Alex Isley"]
}


# SoundSpace curated music library

music_library = {
    "R&B": {
        "artists": [
            "Dijon", "Sampha", "Kelela", "Blood Orange",
            "Snoh Aalegra", "Cleo Sol", "Chloe x Halle",
            "Donell Jones", "Alex Isley", "Ravyn Lenae"
        ],
        "songs": [
            {"title": "Many Times", "artist": "Dijon"},
            {"title": "Spirit 2.0", "artist": "Sampha"},
            {"title": "Contact", "artist": "Kelela"},
            {"title": "Charcoal Baby", "artist": "Blood Orange"},
            {"title": "When I'm in Your Arms", "artist": "Cleo Sol"},
            {"title": "I Want You Around", "artist": "Snoh Aalegra"},
            {"title": "Do It", "artist": "Chloe x Halle"},
            {"title": "The Kids Are Alright", "artist": "Chloe x Halle"},
            {"title": "You Know What's Up", "artist": "Donell Jones"},
            {"title": "Into Orbit", "artist": "Alex Isley"},
            {"title": "Skin Tight", "artist": "Ravyn Lenae"}
        ]
    },

    "Hip-Hop": {
        "artists": [
            "Mac Miller", "Isaiah Rashad", "MAVI", "Aminé",
            "Saba", "Jay-Z", "Kid Cudi", "Kanye West",
            "OutKast", "Earl Sweatshirt", "A$AP Rocky"
        ],
        "songs": [
            {"title": "Woods", "artist": "Mac Miller"},
            {"title": "Heavenly Father", "artist": "Isaiah Rashad"},
            {"title": "Self Love", "artist": "MAVI"},
            {"title": "RICKY", "artist": "Aminé"},
            {"title": "Busy / Sirens", "artist": "Saba"},
            {"title": "Feelin' It", "artist": "Jay-Z"},
            {"title": "30 Hours", "artist": "Kanye West"},
            {"title": "Words2LiveBy", "artist": "Earl Sweatshirt"},
            {"title": "Peso", "artist": "A$AP Rocky"}
        ]
    },

    "Soul": {
        "artists": [
            "Sade", "D'Angelo", "India.Arie", "Lauryn Hill",
            "Groove Theory", "SWV", "Goapele",
            "Grover Washington Jr.", "Marvin Gaye", "Prince",
            "Otis Redding", "Amy Winehouse", "The Isley Brothers"
        ],
        "songs": [
            {"title": "Smooth Operator", "artist": "Sade"},
            {"title": "Brown Sugar", "artist": "D'Angelo"},
            {"title": "Video", "artist": "India.Arie"},
            {"title": "Ex-Factor", "artist": "Lauryn Hill"},
            {"title": "Tell Me", "artist": "Groove Theory"},
            {"title": "Weak", "artist": "SWV"},
            {"title": "Closer", "artist": "Goapele"},
            {"title": "Just the Two of Us", "artist": "Grover Washington Jr."},
            {"title": "What's Going On", "artist": "Marvin Gaye"},
            {"title": "I Wanna Be Your Lover", "artist": "Prince"},
            {"title": "The Dock of the Bay", "artist": "Otis Redding"},
            {"title": "Back to Black", "artist": "Amy Winehouse"},
            {"title": "Between the Sheets", "artist": "The Isley Brothers"}
        ]
    },

    "Jazz": {
        "artists": [
            "Yussef Dayes", "Alfa Mist",
            "BADBADNOTGOOD", "Grover Washington Jr."
        ],
        "songs": [
            {"title": "Black Classical Music", "artist": "Yussef Dayes"},
            {"title": "Keep On", "artist": "Alfa Mist"},
            {"title": "Time Moves Slow", "artist": "BADBADNOTGOOD"},
            {"title": "Mister Magic", "artist": "Grover Washington Jr."}
        ]
    },

    "Pop": {
        "artists": [
            "Frank Ocean", "Blood Orange", "Aminé",
            "Tame Impala", "Kaytranada", "Prince", "Chloe x Halle"
        ],
        "songs": [
            {"title": "Seigfried", "artist": "Frank Ocean"},
            {"title": "Best to You", "artist": "Blood Orange"},
            {"title": "Invincible", "artist": "Aminé"},
            {"title": "The Less I Know the Better", "artist": "Tame Impala"},
            {"title": "Lite Spots", "artist": "Kaytranada"}
        ]
    },

    "Electronic / Rave": {
        "artists": [
            "The Chainsmokers",
            "DJ Snake",
            "Justin Bieber",
            "CHRYSTAL",
            "NOTION",
            "Black Eyed Peas",
            "AlunaGeorge",
            "Jack Ü"
        ],
        "songs": [
            {"title": "Roses", "artist": "The Chainsmokers"},
            {"title": "Middle", "artist": "DJ Snake"},
            {"title": "I'll Show You", "artist": "Justin Bieber"},
            {"title": "The Days (NOTION Remix)", "artist": "CHRYSTAL & NOTION"},
            {"title": "Meet Me Halfway", "artist": "Black Eyed Peas"},
            {"title": "You Know You Like It (DJ Snake Remix)", "artist": "AlunaGeorge & DJ Snake"},
            {"title": "Where Are Ü Now", "artist": "Jack Ü"}
        ]
    }
}


# Page styling
st.markdown("""
<style>
    .stApp {
        background-color: #FAFAF8;
        color: #222222;
    }

    h1, h2, h3, p, label {
        color: #222222;
    }

    .hero {
        padding: 55px 0 35px 0;
    }

    .hero h1 {
        font-size: 52px;
        font-weight: 700;
        letter-spacing: -2px;
        color: #222222;
    }

    .hero p {
        font-size: 18px;
        color: #777777;
    }

    div.stButton > button {
    background-color: #222222 !important;
    color: #FFFFFF !important;
    border-radius: 8px;
    border: none;
    padding: 10px 24px;
}

div.stButton > button p {
    color: #FFFFFF !important;
}
    }
</style>
""", unsafe_allow_html=True)

# Navigation
left, right = st.columns([3, 1])

with left:
    st.markdown("**S O U N D S P A C E**")

with right:
    st.markdown("Discover | Explore")

st.divider()

# Hero section
st.markdown("""
<div class="hero">
    <h1>Find your sound.</h1>
    <p>Discover music, explore new artists, and find your next favorite song.</p>
</div>
""", unsafe_allow_html=True)

# Music discovery
st.subheader("Start discovering")

favorite_artist = st.text_input(
    "Which artist are you listening to lately?",
    placeholder="Enter an artist name..."
)

favorite_genre = st.selectbox(
    "Choose your favorite genre",
    ["R&B", "Hip-Hop", "Soul", "Jazz", "Pop", "Other"]
)


if st.button("Discover Music"):
    if favorite_artist:
        st.success(
            f"You're exploring {favorite_genre} and artists like "
            f"{favorite_artist}. Here are some recommendations for you."
        )

        recommendations = music_library.get(
            favorite_genre,
            {"artists": [], "songs": []}
        )

        st.subheader("Artists to discover")

        matching_artists = artist_connections.get(
            favorite_artist.strip().lower(),
            []
        )

        if not matching_artists:
            matching_artists = [
                artist for artist in recommendations["artists"]
                if artist.lower() != favorite_artist.strip().lower()
            ]

        for artist in matching_artists:
            st.write(f"🎧 {artist}")

        st.subheader("Songs worth hearing")

        matching_songs = [
            song for song in recommendations["songs"]
            if song["artist"].lower() in [
                artist.lower() for artist in matching_artists
            ]
        ]

        if matching_songs:
            for song in matching_songs:
                st.write(f"**{song['title']}** — {song['artist']}")
        else:
            st.write("Explore the genre catalog for more songs!")

    else:
        st.warning("Enter an artist name to get started.")

st.divider()



# Genre exploration

st.subheader("Explore by genre")
st.write("Find your next favorite artist or song.")

genre_names = [
    "R&B",
    "Hip-Hop",
    "Soul",
    "Jazz",
    "Pop",
    "Electronic / Rave"
]

genre_columns = st.columns(3)

for index, genre in enumerate(genre_names):
    with genre_columns[index % 3]:
        if st.button(genre, key=f"genre_{genre}"):
            st.session_state.selected_genre = genre

# Display recommendations

if "selected_genre" in st.session_state:
    selected_genre = st.session_state.selected_genre

    recommendations = music_library.get(
        selected_genre,
        {"artists": [], "songs": []}
    )

    st.divider()
    st.subheader(f"Explore {selected_genre}")

    st.markdown("### Artists to discover")

    artist_columns = st.columns(2)

    for index, artist in enumerate(recommendations["artists"]):
        with artist_columns[index % 2]:
            st.markdown(f"**{artist}**")

    st.markdown("### Songs worth hearing")

    for song in recommendations["songs"]:
        st.markdown(f"**{song['title']}** — {song['artist']}")



# The Listening Room

st.divider()

st.title("The Listening Room")
st.write("Curated listening experiences for wherever your mood takes you.")

listening_rooms = {
    "After Hours": {
        "description": "Late-night sounds, alternative R&B, and electronic music.",
        "artists": ["Frank Ocean", "Sampha", "Dijon", "Kelela"]
    },
    "The Underground": {
        "description": "Independent voices, underground hip-hop, and rave energy.",
        "artists": ["MAVI", "Earl Sweatshirt", "Saba", "DJ Snake"]
    },
    "Soul Searching": {
        "description": "Neo-soul, timeless voices, and music with feeling.",
        "artists": ["Sade", "D'Angelo", "Cleo Sol", "Lauryn Hill"]
    },
    "Somewhere Between": {
        "description": "Alternative sounds that exist between genres.",
        "artists": ["Blood Orange", "Tame Impala", "Kaytranada", "Aminé"]
    }
}

room_columns = st.columns(2)

for index, (room_name, room_info) in enumerate(listening_rooms.items()):
    with room_columns[index % 2]:
        st.subheader(room_name)
        st.write(room_info["description"])

        st.markdown("**Featured artists**")

        for artist in room_info["artists"]:
            st.write(f"🎧 {artist}")


# Footer
st.divider()
st.caption("SoundSpace © 2026 | Discover your next favorite sound.")

