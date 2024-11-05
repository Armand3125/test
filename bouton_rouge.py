import streamlit as st

# Titre de l'application
st.title("Exemple de Bouton Rouge avec Streamlit")

# CSS pour personnaliser le bouton en rouge
st.markdown("""
    <style>
    .stButton > button {
        color: white;
        background-color: red;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Afficher le bouton
if st.button("Cliquez-moi !"):
    # Message affiché lorsque le bouton est cliqué
    st.write("Hello World!")
