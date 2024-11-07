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

# Créer une ligne avec deux groupes de colonnes côte à côte
cols = st.columns([1, 1, 1, 1])  # Quatre colonnes dans une même ligne

# Premier groupe de colonnes (1 et 2)
with cols[0]:
    # Liste des options de couleurs avec cases à cocher sans texte
    color_options = list(pal.values())  # Utiliser les couleurs elles-mêmes comme options
    selected_color_rgb_1 = st.radio("", color_options, index=0)  # Case à cocher sans texte visible

with cols[1]:
    # Affichage des rectangles colorés en face des cases à cocher
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Deuxième groupe de colonnes (3 et 4)
with cols[2]:
    # Liste des options de couleurs avec cases à cocher sans texte
    selected_color_rgb_2 = st.radio("", color_options, index=1)  # Case à cocher sans texte visible

with cols[3]:
    # Affichage des rectangles colorés pour le deuxième ensemble
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Afficher le texte et le carré de couleur sélectionnée pour le premier ensemble de colonnes
if selected_color_rgb_1:
    st.write(f"Vous avez sélectionné la couleur (ensemble 1):")
    st.markdown(
        f"<div style='background-color: rgb{selected_color_rgb_1}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )

# Afficher le texte et le carré de couleur sélectionnée pour le deuxième ensemble de colonnes
if selected_color_rgb_2:
    st.write(f"Vous avez sélectionné la couleur (ensemble 2):")
    st.markdown(
        f"<div style='background-color: rgb{selected_color_rgb_2}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )
