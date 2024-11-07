import streamlit as st

# Palette de couleurs
pal = {
    "Noir Charbon": (0, 0, 0), "Blanc Jade": (255, 255, 255),
    "Jaune Or": (228, 189, 104), "Bleu Cyan": (0, 134, 214),
    "Violet Lila": (174, 150, 212), "Vert Gui": (63, 142, 67),
    "Rouge Ecarlate": (222, 67, 67), "Bleu Marine": (0, 120, 191),
    "Orange Mandarine": (249, 153, 99), "Vert Galaxie": (59, 102, 94),
    "Bleu Glacier": (163, 216, 225), "Violet Magenta": (236, 0, 140),
    "Gris Argent": (166, 169, 170), "Violet Basic": (94, 67, 183),
}

st.title("Sélection de Couleurs")

# Définir le style CSS pour changer la couleur du texte des cases à cocher (texte noir)
css = """
    <style>
        .stRadio label {
            color: black;
            font-weight: normal;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Créer une colonne pour les sélections de couleur
color_options = [f"{name}" for name in pal.keys()]
selected_color_name = st.radio("Choisissez une couleur", color_options)

# Créer une colonne à côté pour afficher la couleur correspondante
cols = st.columns(2)

with cols[1]:
    if selected_color_name:
        rgb = pal[selected_color_name]
        st.write(f"Vous avez sélectionné la couleur : {selected_color_name}")
        st.markdown(
            f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
            unsafe_allow_html=True
        )

# Affichage des couleurs possibles avec leurs petits carrés
with cols[0]:
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"- {color_name} : <div style='background-color: rgb{color_rgb}; width: 20px; height: 20px; display: inline-block; border-radius: 3px;'></div>",
            unsafe_allow_html=True
        )
