import streamlit as st
import pandas as pd
from mplsoccer import VerticalPitch


# to run: python -m streamlit run playerprofile.py

# Load player stats from Excel
@st.cache_data
def load_stats():
    return pd.read_excel("Wollongong Wolves Statistics (Python Version).xlsx")

stats_df = load_stats()

# Player data
players = [
    {
        "Name": "Alex Masciovecchio",
        "dob": "25-09-2001",
        "Height": "",
        "Weight": "",
        "positions": ["RW", "LW", "RWB", "LWB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041024_Wollongong_Masciovecchio.jpg"
    },
    {
        "Name": "Banri Kanaizumi",
        "dob": "04-05-1993",
        "Height": "182",
        "Weight": "",
        "positions": ["CB", "LCB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041177_Wollongong_Kanaizumi.jpg"
    },
    {
        "Name": "Ben Giason",
        "dob": "29-09-2004",
        "Height": "",
        "Weight": "",
        "positions": ["RB", "LB", "RW", "LCB", "LCM", "LDM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041284_Wollongong_Giason.jpg"
    },
    {
        "Name": "Damon Gray",
        "dob": "28-03-2005",
        "Height": "",
        "Weight": "",
        "positions": ["LS", "LW", "ST", "RW"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041313_Wollongong_.jpg"
    },
    {
        "Name": "Darcy Madden",
        "dob": "17-04-1996",
        "Height": "188",
        "Weight": "",
        "positions": ["DM", "LDM", "RB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041047_Wollongong_Madden.jpg"
    },
    {
        "Name": "Dax Kelly",
        "dob": "04-06-2003",
        "Height": "",
        "Weight": "",
        "positions": ["RB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041127_Wollongong_-1.jpg"
    },
    {
        "Name": "Dylan King",
        "dob": "2007",
        "Height": "",
        "Weight": "",
        "positions": ["RW"],
        "image": ""
    },
    {
        "Name": "Dylan Ryan",
        "dob": "10-06-2000",
        "Height": "184",
        "Weight": "75",
        "positions": ["LB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041037_Wollongong_.jpg"
    },
    {
        "Name": "Harrison Buesnel",
        "dob": "28-06-2003",
        "Height": "188",
        "Weight": "",
        "positions": ["RCB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041251_Wollongong_Buesnel.jpg"
    },
    {
        "Name": "James Anagnostopoulos",
        "dob": "2004",
        "Height": "",
        "Weight": "",
        "positions": ["RCM", "LCM", "CM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041154_Wollongong_.jpg"
    },
    {
        "Name": "Lachlan Scott",
        "dob": "15-04-1997",
        "Height": "180",
        "Weight": "",
        "positions": ["ST", "RS"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041229_Wollongong_Scott.jpg"
    },
    {
        "Name": "Liam Ball",
        "dob": "2005",
        "Height": "",
        "Weight": "",
        "positions": ["CAM", "LCM"],
        "image": ""
    },
    {
        "Name": "Lucas Trajcevski",
        "dob": "2006",
        "Height": "",
        "Weight": "",
        "positions": ["LW"],
        "image": ""
    },
    {
        "Name": "Marcus Beattie",
        "dob": "01-04-1996",
        "Height": "",
        "Weight": "",
        "positions": ["RWB", "RW", "RB", "RCM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041296_Wollongong_Beattie.jpg"
    },
    {
        "Name": "Nicholas Olsen",
        "dob": "26-09-1995",
        "Height": "175",
        "Weight": "",
        "positions": ["CAM", "LW", "RW", "CM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041262_Wollongong_Olsen.jpg"
    },
    {
        "Name": "Oliver Yates",
        "dob": "20-01-2003",
        "Height": "195",
        "Weight": "",
        "positions": ["GK"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041141_Wollongong_.jpg"
    },
    {
        "Name": "Raphael Lea'i",
        "dob": "09-09-2003",
        "Height": "176",
        "Weight": "60",
        "positions": ["RW", "LW", "RS", "LWB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041324_Wollongong_LEAI.jpg"
    },
    {
        "Name": "Sebastian Duarte",
        "dob": "2006",
        "Height": "",
        "Weight": "",
        "positions": ["LB"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041072_Wollongong_Duarte.jpg"
    },
    {
        "Name": "Sebastian Hernandez",
        "dob": "2003",
        "Height": "183",
        "Weight": "",
        "positions": ["LW", "RW"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041059_Wollongong_Hernandez.jpg"
    },
    {
        "Name": "Sim Woon Sub",
        "dob": "24-02-1990",
        "Height": "176",
        "Weight": "",
        "positions": ["RDM", "CDM"],
        "image": "https://wollongongwolves.com.au/wp-content/uploads/db202502041099_Wollongong_.jpg"
    }
]


# Dropdown mapping
player_options = {player["Name"]: player for player in players}

# Position coordinates for the pitch map
positions_coords = {
    'GK': (40, 10), 'CB': (40, 25), 'LCB': (25, 25), 'RCB': (55, 25),
    'RB': (75, 34), 'LB': (5, 34), 'LWB': (5, 60), 'LW': (5, 90),
    'RWB': (75, 60), 'RW': (75, 90), 'LDM': (25, 43), 'CDM': (40, 43),
    'RDM': (55, 43), 'LCM': (25, 60), 'CM': (40, 60), 'RCM': (55, 60),
    'LAM': (25, 79), 'CAM': (40, 79), 'RAM': (55, 79), 'ST': (40, 106),
    'RS': (55, 106), 'LS': (25, 106)
}

# Styling
st.markdown("""
    <style>
        .header-logo {
            position: absolute;
            top: 5px;
            right: 5px;
            z-index: 100;
        }
        .player-info {
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            text-align: left;
            margin-left: 20px;
        }
        .player-info img {
            margin-bottom: 10px;
        }
        .selectbox-container {
            width: 100%;
            margin-bottom: 20px;
        }
        .selectbox-container select {
            width: 100%;
            font-size: 16px;
            padding: 10px;
            background-color: #28252C;
            color: white;
            border: none;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown('<img class="header-logo" src="https://upload.wikimedia.org/wikipedia/en/e/ed/Wollongong_Wolves_FC.jpg" width="70" />', unsafe_allow_html=True)

# Page Title
st.title("Wollongong Wolves Player Dashboard")

# Create columns for layout: one for the player info and another for the pitch
col1, col2 = st.columns([1, 2])

with col1:
    # Add a container for the selectbox
    selected_name = st.selectbox("Select a Player", list(player_options.keys()), key="player_selector")
    selected_player = player_options[selected_name]

    # Display player info
    st.markdown(f"""
        <div class='player-info'>
            <img src='{selected_player['image']}' width='250'/>
            <div>
                <p><strong>Date of Birth:</strong> {selected_player['dob']}</p>
                <p><strong>Height:</strong> {selected_player['Height']} cm</p>
                <p><strong>Weight:</strong> {selected_player['Weight']} kg</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Create the pitch layout
    pitch = VerticalPitch(half=False)
    fig, ax = pitch.draw(figsize=(7, 6))
    ax.set_facecolor("#28252C")

    for pos_label, coord in positions_coords.items():
        color = "green" if pos_label in selected_player["positions"] else "black"
        ax.scatter(coord[0], coord[1], color=color, s=500, edgecolor="white")
        ax.text(coord[0], coord[1], pos_label, ha="center", va="center", fontsize=10, color="white")

    st.pyplot(fig)

# Player stats displayed below the pitch
selected_player_stats = stats_df[stats_df['Name'] == selected_name]
selected_player_stats = selected_player_stats.sort_values(by='Round', ascending=False)

# Format percentage columns into % with 0 decimal places for both stats_df and selected_player_stats
percentage_columns = ['Dribble %', 'Pass %', 'Cross %', 'Long Ball %', 'Ground Duel %', 'Aerial Duel %']

# Format in stats_df first
for col in percentage_columns:
    if col in stats_df.columns:
        stats_df[col] = stats_df[col].apply(lambda x: f"{x * 100:.0f}%" if pd.notnull(x) else "")

# Now apply to the selected_player_stats DataFrame
for col in percentage_columns:
    if col in selected_player_stats.columns:
        selected_player_stats[col] = selected_player_stats[col].apply(lambda x: f"{x * 100:.0f}%" if pd.notnull(x) else "")



# Reorder columns to pin 'Round' and 'Opponent' at the beginning
columns_order = ['Round', 'Opponent'] + [col for col in selected_player_stats.columns if col not in ['Round', 'Opponent']]
selected_player_stats = selected_player_stats[columns_order]

# Calculate total minutes played
total_minutes = selected_player_stats['Minutes'].sum() if 'Minutes' in selected_player_stats.columns else 0
st.subheader(f"Total Minutes Played: {total_minutes}")

if not selected_player_stats.empty:
    st.subheader("Player Statistics (By Match)")
    st.dataframe(selected_player_stats.drop(columns=["Name"]), use_container_width=True)
else:
    st.warning("No stats found in the Excel file for this player.")




# ── Total STATS ────────────────────────────────────────────────────────────────
@st.cache_data
def load_Total_stats():
    return pd.read_excel("Wollongong Wolves Statistics Total.xlsx")

Total_df = load_Total_stats()

# Filter to the chosen player
selected_player_Total = Total_df[Total_df["Name"] == selected_name].copy()

# ▸ 1. percentages ➜ "85%" style
for col in percentage_columns:
    if col in selected_player_Total.columns:
        selected_player_Total[col] = selected_player_Total[col].apply(
            lambda x: f"{x * 100:.0f}%" if pd.notnull(x) else ""
        )

# ▸ 2. everything else ➜ two‑decimal numbers (x.xx)
for col in selected_player_Total.columns:
    if col not in percentage_columns + ["Name"]:
        selected_player_Total[col] = selected_player_Total[col].apply(
            lambda x: f"{x:.2f}" if pd.notnull(x) else ""
        )

# ▸ 3. show it
if not selected_player_Total.empty:
    st.subheader("Player Statistics (Total)")
    st.dataframe(selected_player_Total.drop(columns=["Name"]), use_container_width=True)
else:
    st.warning("No Total statistics available for this player.")





# ── PER‑90 STATS ────────────────────────────────────────────────────────────────
@st.cache_data
def load_per90_stats():
    return pd.read_excel("Wollongong Wolves Statistics per 90.xlsx")

per90_df = load_per90_stats()

# Filter to the chosen player
selected_player_per90 = per90_df[per90_df["Name"] == selected_name].copy()

# ▸ 1. percentages ➜ "85%" style
for col in percentage_columns:
    if col in selected_player_per90.columns:
        selected_player_per90[col] = selected_player_per90[col].apply(
            lambda x: f"{x * 100:.0f}%" if pd.notnull(x) else ""
        )

# ▸ 2. everything else ➜ two‑decimal numbers (x.xx)
for col in selected_player_per90.columns:
    if col not in percentage_columns + ["Name"]:
        selected_player_per90[col] = selected_player_per90[col].apply(
            lambda x: f"{x:.2f}" if pd.notnull(x) else ""
        )

# ▸ 3. show it
if not selected_player_per90.empty:
    st.subheader("Player Statistics (Per 90)")
    st.dataframe(selected_player_per90.drop(columns=["Name"]), use_container_width=True)
else:
    st.warning("No per 90 statistics available for this player.")





# Define KPIs by position (your existing dictionary)
kpi_by_position = {
    "GK": [
        "Saves", "Shots Faced", "Goals Conceded", "xGOT Faced", "xG Prevented", "Passes", "Passes Att.",
        "Pass %", "Long Balls", "Long Balls Att.", "Long Ball %", "Clearances", "PAdj Interceptions"
    ],
    "FB": [
        "xA", "Assists", "Dribbles", "Dribbles Att.", "Dribble %", "Passes", "Passes Att.", "Pass %",
        "Key Passes", "Crosses", "Crosses Att.", "Cross %", "Long Balls", "Long Balls Att.", "Long Ball %",
        "Ground Duels", "Ground Duels Att.", "Ground Duel %", "Aerial Duels", "Aerial Duels Att.",
        "Aerial Duel %", "Fouls", "Was Fouled", "Clearances", "Blocked Shots", "Dribbled Past",
        "PAdj Interceptions", "PAdj Tackles"
    ],
    "CB": [
        "Passes", "Passes Att.", "Pass %", "Long Balls", "Long Balls Att.", "Long Ball %",
        "Ground Duels", "Ground Duels Att.", "Ground Duel %", "Aerial Duels", "Aerial Duels Att.",
        "Aerial Duel %", "Fouls", "Was Fouled", "Clearances", "Blocked Shots", "Dribbled Past",
        "PAdj Interceptions", "PAdj Tackles"
    ],
    "DM": [
        "Dribbles", "Dribbles Att.", "Dribble %", "Passes", "Passes Att.", "Pass %", "Key Passes",
        "Big Chances Created", "Long Balls", "Long Balls Att.", "Long Ball %", "Ground Duels",
        "Ground Duels Att.", "Ground Duel %", "Aerial Duels", "Aerial Duels Att.", "Aerial Duel %",
        "Fouls", "Was Fouled", "Clearances", "Blocked Shots", "Dribbled Past",
        "PAdj Interceptions", "PAdj Tackles"
    ],
    "CM": [
        "xG", "xA", "Goals", "Assists", "Shots On Target", "Total Shots", "Dribbles", "Dribbles Att.",
        "Dribble %", "Passes", "Passes Att.", "Pass %", "Key Passes", "Big Chances Created",
        "Long Balls", "Long Balls Att.", "Long Ball %", "Ground Duels", "Ground Duels Att.",
        "Ground Duel %", "Aerial Duels", "Aerial Duels Att.", "Aerial Duel %", "Fouls",
        "Was Fouled", "Clearances", "Blocked Shots", "Dribbled Past",
        "PAdj Interceptions", "PAdj Tackles"
    ],
    "AM": [
        "xG", "xA", "Goals", "Assists", "Shots On Target", "Total Shots", "Dribbles", "Dribbles Att.",
        "Dribble %", "Passes", "Passes Att.", "Pass %", "Key Passes", "Big Chances Created",
        "Crosses", "Crosses Att.", "Cross %", "Long Balls", "Long Balls Att.",
        "Long Ball %", "Ground Duels", "Ground Duels Att.", "Ground Duel %",
        "Aerial Duels", "Aerial Duels Att.", "Aerial Duel %", "Fouls", "Was Fouled", "Offsides",
        "Dribbled Past", "PAdj Interceptions", "PAdj Tackles"
    ],
    "W": [
        "xG", "xA", "Goals", "Assists", "Shots On Target", "Total Shots", "Dribbles", "Dribbles Att.",
        "Dribble %", "Passes", "Passes Att.", "Pass %", "Key Passes", "Big Chances Created",
        "Crosses", "Crosses Att.", "Cross %", "Ground Duels", "Ground Duels Att.",
        "Ground Duel %", "Aerial Duels", "Aerial Duels Att.", "Aerial Duel %", "Fouls",
        "Was Fouled", "Offsides", "Dribbled Past", "PAdj Interceptions", "PAdj Tackles"
    ],
    "ST": [
        "xG", "xA", "Goals", "Assists", "Shots On Target", "Total Shots", "Dribbles", "Dribbles Att.",
        "Dribble %", "Passes", "Passes Att.", "Pass %", "Key Passes", "Big Chances Created",
        "Ground Duels", "Ground Duels Att.", "Ground Duel %", "Aerial Duels", "Aerial Duels Att.",
        "Aerial Duel %", "Fouls", "Was Fouled", "Offsides", "Dribbled Past",
        "PAdj Interceptions", "PAdj Tackles"
    ]
}

# Define KPI categories explicitly
kpi_categories = {
    "Shooting": [
        "xG", "Goals", "Shots On Target", "Total Shots",
    ],
    "Creation": [
        "xA", "Assists", "Big Chances Created", "Key Passes", "Crosses", "Crosses Att.", "Cross %"
    ],
    "Progression": [
        "Dribbles", "Dribbles Att.", "Dribble %", "Was Fouled", "Offsides"
    ],
    "Passing": [
        "Passes", "Passes Att.", "Pass %", "Long Balls", "Long Balls Att.", "Long Ball %"
    ],
    "Duels": [
        "Ground Duels", "Ground Duels Att.", "Ground Duel %", "Aerial Duels", "Aerial Duels Att.", "Aerial Duel %"
    ],
    "Defence": [
        "Fouls", "Clearances", "PAdj Interceptions", "PAdj Tackles", "Dribbled Past", "Blocked Shots"
    ],
    "Goalkeeping": [
        "Saves", "Shots Faced", "Goals Conceded", "xGOT Faced", "xG Prevented"
    ]
}

# Load benchmark data
@st.cache_data
def load_benchmark():
    return pd.read_excel("NPL NSW 2025 May Position Benchmarks.xlsx")

benchmark_df = load_benchmark()

# Dropdown for benchmark position
all_positions = sorted(benchmark_df['Position'].unique())
selected_benchmark_position = st.selectbox("Select position to compare with:", all_positions)

# Get player info
selected_name = selected_player["Name"]
selected_positions = selected_player["positions"]

# Filter benchmark data for selected benchmark position
def position_filter(pos_string, benchmark_position):
    return benchmark_position in pos_string

benchmark_filtered = benchmark_df[benchmark_df['Position'].apply(lambda x: position_filter(x, selected_benchmark_position))]

# Get player row (from full benchmark data, regardless of position)
player_benchmark_row = benchmark_df[benchmark_df['Name'] == selected_name]

if player_benchmark_row.empty:
    st.warning(f"No data found for player {selected_name}")
else:
    # KPIs for the selected benchmark position, intersect with columns present in dataframe
    selected_kpis = [kpi for kpi in kpi_by_position.get(selected_benchmark_position, []) if kpi in benchmark_df.columns]

    # Filter numeric KPIs only present for this player
    numeric_kpis = [kpi for kpi in selected_kpis if pd.api.types.is_numeric_dtype(benchmark_df[kpi])]

    # Prepare categories that have KPIs to show
    categories_with_kpis = [cat for cat, cat_kpis in kpi_categories.items() if any(kpi in numeric_kpis for kpi in cat_kpis)]

    # Define how many columns per row
    cols_per_row = 3
    rows = (len(categories_with_kpis) + cols_per_row - 1) // cols_per_row

    for row_idx in range(rows):
        cols = st.columns(cols_per_row)
        for col_idx in range(cols_per_row):
            cat_idx = row_idx * cols_per_row + col_idx
            if cat_idx >= len(categories_with_kpis):
                break

            category = categories_with_kpis[cat_idx]
            category_kpis = kpi_categories[category]
            kpis_to_show = [kpi for kpi in category_kpis if kpi in numeric_kpis]
            if not kpis_to_show:
                continue

            percentile_data = {}
            for kpi in kpis_to_show:
                player_value = player_benchmark_row.iloc[0][kpi]
                percentile_rank = (benchmark_filtered[kpi] <= player_value).mean() * 100
                percentile_data[kpi] = f"{percentile_rank:.1f}th percentile"

            percentile_df = pd.DataFrame.from_dict(percentile_data, orient='index', columns=['Percentile Rank'])

            def color_percentile_html(val):
                percentile_num = float(val.split('th')[0])
                red = int(255 * (100 - percentile_num) / 100)
                green = int(255 * percentile_num / 100)
                blue = 0
                color = f"rgb({red},{green},{blue})"
                return f'<div style="background-color:{color}; padding:6px; border-radius:4px;">{val}</div>'

            percentile_df['Percentile Rank'] = percentile_df['Percentile Rank'].apply(color_percentile_html)
            html_table = percentile_df.to_html(escape=False)

            with cols[col_idx]:
                st.subheader(f"{category}")
                st.markdown(html_table, unsafe_allow_html=True)

    # Final combined percentile table for all numeric KPIs
    percentile_data = {}
    for kpi in numeric_kpis:
        player_value = player_benchmark_row.iloc[0][kpi]
        percentile_rank = (benchmark_filtered[kpi] <= player_value).mean() * 100
        percentile_data[kpi] = f"{percentile_rank:.1f}th percentile"

    st.subheader(f"Percentile Ranks for {selected_name} vs. {selected_benchmark_position} NPL NSW players with 500+ Season Minutes by R15")

    percentile_df = pd.DataFrame.from_dict(percentile_data, orient='index', columns=['Percentile Rank'])

    def color_percentile_html(val):
        percentile_num = float(val.split('th')[0])
        red = int(255 * (100 - percentile_num) / 100)
        green = int(255 * percentile_num / 100)
        blue = 0
        color = f"rgb({red},{green},{blue})"
        return f'<div style="background-color:{color}; padding:6px; border-radius:4px;">{val}</div>'

    percentile_df['Percentile Rank'] = percentile_df['Percentile Rank'].apply(color_percentile_html)
    html_table = percentile_df.to_html(escape=False)
    st.markdown(html_table, unsafe_allow_html=True)


# Pre-defined disclaimer text
disclaimer ="""
Disclaimers:
- Sofascore stat definitions: https://x.com/SofascoreINT/status/1239950999420375040
- All event data is collected from Sofascore. The data from NPL NSW matches is gathered by data collectors who watch the YouTube stream. If the stream cuts out, they are unable to collect the event data that occurs during those moments.
- The data collected for this app is typically available 3-4 days after the match is played.

Missing Data:
- Cup matches. The data is only from NPL NSW matches.
- Match data for Round 2: Wollongong Wolves vs. St George City FA.
- Lachlan Scott's 48th-minute goal from Round 10: Wollongong Wolves vs. Sutherland Sharks.
- Expected Goals on Target (xGOT) from Round 12: Wollongong Wolves vs. Mt Druitt Town Rangers.
"""

# Display disclaimer at the bottom
st.write("### Disclaimers & Missing Data")
st.write(disclaimer)
