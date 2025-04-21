import streamlit as st
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch

# Set the page config
st.set_page_config(page_title="Wollongong Wolves Player Dashboard", layout="wide")

# Sample player data (20 total)
players = [
    {
        "name": "Alex Masciovecchio",
        "dob": "25-09-2001",
        "Height": "",
        "Weight": "",
        "positions": ["RW", "LW", "RWB", "LWB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041024_Wollongong_Masciovecchio.jpg"
    },
    {
        "name": "Banri Kanaizumi",
        "dob": "04-05-1993",
        "Height": "182",
        "Weight": "",
        "positions": ["CB", "LCB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041177_Wollongong_Kanaizumi.jpg"
    },
    {
        "name": "Ben Giason",
        "dob": "29-09-2004",
        "Height": "",
        "Weight": "",
        "positions": ["RB", "LB", "RW", "LCB", "LCM", "LDM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041284_Wollongong_Giason.jpg"
    },
    {
        "name": "Damon Gray",
        "dob": "28-03-2005",
        "Height": "",
        "Weight": "",
        "positions": ["LS", "LW", "ST", "RW"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041313_Wollongong_.jpg"
    },
    {
        "name": "Darcy Madden",
        "dob": "17-04-1996",
        "Height": "188",
        "Weight": "",
        "positions": ["DM", "LDM", "RB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041047_Wollongong_Madden.jpg"
    },
    {
        "name": "Dax Kelly",
        "dob": "04-06-2003",
        "Height": "",
        "Weight": "",
        "positions": ["RB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041127_Wollongong_-1.jpg"
    },
    {
        "name": "Dylan King",
        "dob": "2007",
        "Height": "",
        "Weight": "",
        "positions": ["RW"],
        "image": ""
    },
    {
        "name": "Dylan Ryan",
        "dob": "10-06-2000",
        "Height": "184",
        "Weight": "75",
        "positions": ["LB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041037_Wollongong_.jpg"
    },
    {
        "name": "Harrison Buesnel",
        "dob": "28-06-2003",
        "Height": "188",
        "Weight": "",
        "positions": ["RCB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041251_Wollongong_Buesnel.jpg"
    },
    {
        "name": "James Anagnostopoulos",
        "dob": "2004",
        "Height": "",
        "Weight": "",
        "positions": ["RCM", "LCM", "CM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041154_Wollongong_.jpg"
    },
    {
        "name": "Lachlan Scott",
        "dob": "15-04-1997",
        "Height": "180",
        "Weight": "",
        "positions": ["ST", "RS"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041229_Wollongong_Scott.jpg"
    },
    {
        "name": "Liam Ball",
        "dob": "2005",
        "Height": "",
        "Weight": "",
        "positions": ["CAM", "LCM"],
        "image": ""
    },
    {
        "name": "Lucas Trajcevski",
        "dob": "2006",
        "Height": "",
        "Weight": "",
        "positions": ["LW"],
        "image": ""
    },
    {
        "name": "Marcus Beattie",
        "dob": "01-04-1996",
        "Height": "",
        "Weight": "",
        "positions": ["RWB", "RW", "RB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041296_Wollongong_Beattie.jpg"
    },
    {
        "name": "Nicholas Olsen",
        "dob": "26-09-1995",
        "Height": "175",
        "Weight": "",
        "positions": ["CAM", "LW", "RW", "CM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041262_Wollongong_Olsen.jpg"
    },
    {
        "name": "Oliver Yates",
        "dob": "20-01-2003",
        "Height": "195",
        "Weight": "",
        "positions": ["GK"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041141_Wollongong_.jpg"
    },
    {
        "name": "Raphael Lea'i",
        "dob": "09-09-2003",
        "Height": "176",
        "Weight": "60",
        "positions": ["RW", "LW", "RS", "LWB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041324_Wollongong_LEAI.jpg"
    },
    {
        "name": "Sebastian Duarte",
        "dob": "2006",
        "Height": "",
        "Weight": "",
        "positions": ["LB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041072_Wollongong_Duarte.jpg"
    },
    {
        "name": "Sebastian Hernandez",
        "dob": "2003",
        "Height": "183",
        "Weight": "",
        "positions": ["LW", "RW"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041059_Wollongong_Hernandez.jpg"
    },
    {
        "name": "Sim Woon Sub",
        "dob": "24-02-1990",
        "Height": "176",
        "Weight": "",
        "positions": ["RDM", "CDM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041099_Wollongong_.jpg"
    }
]

# Dropdown dictionary
player_options = {player["name"]: player for player in players}

# Position coordinates
positions_coords = {
    'GK': (40, 10), 'CB': (40, 25), 'LCB': (25, 25), 'RCB': (55, 25),
    'RB': (75, 34), 'LB': (5, 34), 'LWB': (5, 60), 'LW': (5, 90),
    'RWB': (75, 60), 'RW': (75, 90), 'LDM': (25, 43), 'CDM': (40, 43),
    'RDM': (55, 43), 'LCM': (25, 60), 'CM': (40, 60), 'RCM': (55, 60),
    'LAM': (25, 79), 'CAM': (40, 79), 'RAM': (55, 79), 'ST': (40, 106),
    'RS': (55, 106), 'LS': (25, 106)
}

# Styling
st.markdown(
    """
    <style>
        .header-logo {
            position: absolute;
            top: 5px;
            right: 5px;
            z-index: 100;
        }
        .stApp {
            padding-top: 80px;
        }
        .player-info {
            margin-top: 20px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
        }
        .player-info img {
            margin-right: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
st.markdown('<img class="header-logo" src="https://upload.wikimedia.org/wikipedia/en/e/ed/Wollongong_Wolves_FC.jpg" width="70" />', unsafe_allow_html=True)

# Title
st.title("Wollongong Wolves Player Dashboard")

# Layout columns
col1, col2 = st.columns([3, 2])

with col1:
    selected_name = st.selectbox("Select a Player", list(player_options.keys()))
    selected_player = player_options[selected_name]

    # Player Info
    st.markdown(f"<div class='player-info'>"
                f"<img src='{selected_player['image']}' width='250'/>"
                f"<div>"
                f"<h3>{selected_player['name']}</h3>"
                f"<p><strong>Date of Birth:</strong> {selected_player['dob']}</p>"
                f"<p><strong>Height:</strong> {selected_player['Height']} cm</p>"
                f"<p><strong>Weight:</strong> {selected_player['Weight']} kg</p>"
                f"<p><strong>Positions:</strong> {', '.join(selected_player['positions'])}</p>"
                f"</div>"
                f"</div>", unsafe_allow_html=True)

with col2:
    pitch = VerticalPitch(half=False)
    fig, ax = pitch.draw(figsize=(7, 6))
    ax.set_facecolor("#28252C")

    for pos_label, coord in positions_coords.items():
        color = "green" if pos_label in selected_player["positions"] else "black"
        ax.scatter(coord[0], coord[1], color=color, s=500, edgecolor="white")
        ax.text(coord[0], coord[1], pos_label, ha="center", va="center", fontsize=10, color="white")

    st.pyplot(fig)
