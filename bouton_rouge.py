import streamlit as st

# Titre de l'application
st.title("Exemple de Bouton avec Couleur RGB Personnalisée")

# CSS pour personnaliser le bouton avec une couleur RGB spécifique
st.markdown("""
    <style>
    .stButton > button {
        color: white;
        background-color: rgb(200, 50, 100);
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
