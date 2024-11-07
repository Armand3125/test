import streamlit as st

pal = {
    "NC": (0, 0, 0), "BJ": (255, 255, 255),
    "JO": (228, 189, 104), "BC": (0, 134, 214),
    "VL": (174, 150, 212), "VG": (63, 142, 67),
    "RE": (222, 67, 67), "BM": (0, 120, 191),
    "OM": (249, 153, 99), "VG": (59, 102, 94),
    "BG": (163, 216, 225), "VM": (236, 0, 140),
    "GA": (166, 169, 170), "VB": (94, 67, 183),
}

st.title("Sélection de Couleurs")

css = """
    <style>
        .stRadio label {
            color: black;
            font-weight: normal;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

cols = st.columns([1, 1, 1, 1])

# Première colonne - choix de la première couleur
with cols[0]:
    color_options = [name for name in pal.keys()]  # Liste des couleurs
    selected_color_name_1 = st.radio("Choisissez une couleur", color_options, key="radio_1")  # ID unique pour cette colonne

with cols[1]:
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Deuxième colonne - choix de la deuxième couleur
with cols[2]:
    selected_color_name_2 = st.radio("Choisissez une autre couleur", color_options, key="radio_2")  # ID unique pour cette colonne

with cols[3]:
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Affichage du carré de couleur et du texte pour la première sélection
if selected_color_name_1:
    rgb1 = pal[selected_color_name_1]
    st.write(f"Vous avez sélectionné la couleur (ensemble 1) : {selected_color_name_1}")
    st.markdown(
        f"<div style='background-color: rgb{rgb1}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )

# Affichage du carré de couleur et du texte pour la deuxième sélection
if selected_color_name_2:
    rgb2 = pal[selected_color_name_2]
    st.write(f"Vous avez sélectionné la couleur (ensemble 2) : {selected_color_name_2}")
    st.markdown(
        f"<div style='background-color: rgb{rgb2}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )
