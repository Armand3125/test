import streamlit as st

# Créer 3 boutons avec des couleurs spécifiques
st.markdown("""
    <style>
    .red-button > button {
        background-color: red;
        color: white;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }
    .yellow-button > button {
        background-color: yellow;
        color: black;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }
    .blue-button > button {
        background-color: blue;
        color: white;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Affichage des boutons avec couleurs
if st.button("Rouge", key="red_button", help="Cliquez pour choisir la couleur rouge"):
    st.markdown('<div class="red-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune", key="yellow_button", help="Cliquez pour choisir la couleur jaune"):
    st.markdown('<div class="yellow-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu", key="blue_button", help="Cliquez pour choisir la couleur bleue"):
    st.markdown('<div class="blue-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Bleue.")
