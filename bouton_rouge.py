import streamlit as st

# Appliquer des styles CSS pour colorer les boutons
st.markdown("""
    <style>
    /* Style général pour tous les boutons */
    .stButton > button {
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }

    /* Style spécifique pour le premier bouton (Rouge) */
    .stButton#red_button > button {
        background-color: red;
        color: white;
    }

    /* Style spécifique pour le deuxième bouton (Jaune) */
    .stButton#yellow_button > button {
        background-color: yellow;
        color: black;
    }

    /* Style spécifique pour le troisième bouton (Bleu) */
    .stButton#blue_button > button {
        background-color: blue;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Créer les boutons avec des clés uniques pour appliquer un style spécifique
if st.button("Rouge", key="red_button"):
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune", key="yellow_button"):
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu", key="blue_button"):
    st.write("Vous avez choisi la couleur Bleue.")
