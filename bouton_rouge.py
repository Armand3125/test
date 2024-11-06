import streamlit as st
import random

# Initialisation de l'état de session
st.session_state.setdefault("button_clicked", False)
st.session_state.setdefault("button_color", "rgb(200, 50, 100)")

# Palette de couleurs
palette = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

# Fonction pour choisir une couleur aléatoire dans la palette
def get_random_color():
    color_name, color_value = random.choice(list(palette.items()))
    return f"rgb{color_value}"

# Définir la couleur du bouton
if st.button("Cliquez-moi !"):
    st.session_state.button_clicked = not st.session_state.button_clicked
    # Changer la couleur du bouton à chaque clic
    st.session_state.button_color = get_random_color()

# Affichage du bouton avec la couleur actuelle
st.markdown(f"""
    <style>
    .stButton > button {{
        color: white;
        background-color: {st.session_state.button_color};
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Exemple de Bouton Toggle avec Streamlit")

# Message affiché si le bouton est cliqué
if st.session_state.button_clicked:
    st.write("Hello World!")
