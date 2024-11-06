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
        color: white;  /* Met le texte en blanc par défaut */
    }

    /* Style pour le premier bouton (Rouge) */
    .stButton:nth-child(1) > button {
        background-color: red;
        color: white;
    }

    /* Style pour le deuxième bouton (Jaune) */
    .stButton:nth-child(2) > button {
        background-color: yellow;
        color: black;  /* Change la couleur du texte à noir pour un meilleur contraste */
    }

    /* Style pour le troisième bouton (Bleu) */
    .stButton:nth-child(3) > button {
        background-color: blue;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Créer les boutons avec Streamlit
if st.button("Rouge"):
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune"):
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu"):
    st.write("Vous avez choisi la couleur Bleue.")
