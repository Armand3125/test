import streamlit as st

# Créer 3 boutons avec des couleurs spécifiques
st.markdown("""
    <style>
    .stButton > button {
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }
    .button-red > button {
        background-color: red;
        color: white;
    }
    .button-yellow > button {
        background-color: yellow;
        color: black;
    }
    .button-blue > button {
        background-color: blue;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Affichage des boutons avec couleurs
if st.button("Rouge", key="red_button", help="Cliquez pour choisir la couleur rouge"):
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune", key="yellow_button", help="Cliquez pour choisir la couleur jaune"):
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu", key="blue_button", help="Cliquez pour choisir la couleur bleue"):
    st.write("Vous avez choisi la couleur Bleue.")
