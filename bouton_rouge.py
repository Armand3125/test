import streamlit as st

# Appliquer des styles CSS pour colorer les boutons
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

# Créer les boutons avec Streamlit et affecter un style via la classe CSS
if st.button("Rouge", key="red_button"):
    st.markdown('<div class="red-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Rouge.")

if st.button("Jaune", key="yellow_button"):
    st.markdown('<div class="yellow-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Jaune.")

if st.button("Bleu", key="blue_button"):
    st.markdown('<div class="blue-button"></div>', unsafe_allow_html=True)
    st.write("Vous avez choisi la couleur Bleue.")
