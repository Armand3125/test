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

    /* Style spécifique pour chaque bouton */
    .red-button > button {
        background-color: red;
        color: white;
    }
    .yellow-button > button {
        background-color: yellow;
        color: black;
    }
    .blue-button > button {
        background-color: blue;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Créer des boutons avec des classes CSS spécifiques
if st.button("Rouge", key="red_button"):
    st.markdown('<div class="red-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune", key="yellow_button"):
    st.markdown('<div class="yellow-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu", key="blue_button"):
    st.markdown('<div class="blue-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Bleue.")
