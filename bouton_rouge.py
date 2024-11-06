import streamlit as st

# Appliquer des styles CSS pour colorer les boutons
st.markdown("""
    <style>
    .stButton > button {
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }
    .stButton:nth-child(1) > button {
        background-color: red;
        color: white;
    }
    .stButton:nth-child(2) > button {
        background-color: yellow;
        color: black;
    }
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
