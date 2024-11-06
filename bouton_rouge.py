import streamlit as st

# Initialiser l'état du bouton dans session_state si ce n'est pas déjà fait
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Titre de l'application
st.title("Exemple de Bouton Toggle avec Streamlit")

# CSS pour personnaliser le bouton en rouge
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

# Afficher le bouton avec fonctionnalité toggle
if st.button("Cliquez-moi !"):
    # Inverser l'état du bouton dans session_state
    st.session_state.button_clicked = not st.session_state.button_clicked

# Afficher ou masquer "Hello World" en fonction de l'état du bouton
if st.session_state.button_clicked:
    st.write("Hello World!")
