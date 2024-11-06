import streamlit as st
import random

st.session_state.setdefault("button_clicked", False)
st.session_state.setdefault("button_color", "rgb(200, 50, 100)")
st.session_state.setdefault("selected_color_name", "Couleur par défaut")

palette = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

def get_random_color():
    color_name, color_value = random.choice(list(palette.items()))
    return f"rgb{color_value}", color_name

if st.button(""):
    st.session_state.button_clicked = not st.session_state.button_clicked
    st.session_state.button_color, st.session_state.selected_color_name = get_random_color()

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

if st.session_state.button_clicked:
    st.write(f"Couleur du bouton : {st.session_state.selected_color_name} - {st.session_state.button_color}")
