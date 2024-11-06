import streamlit as st

# Initialiser l'état du bouton dans session_state si ce n'est pas déjà fait
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Titre de l'application
st.title("Exemple de Bouton Toggle avec Changement de Couleur")

# CSS pour personnaliser le bouton : transparent par défaut, rouge après le clic
st.markdown("""
    <style>
    .stButton > button {
        color: white;
        background-color: rgba(0, 0, 0, 0); /* Transparent au départ */
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
        transition: background-color 0.3s ease; /* Animation de transition */
    }
    .stButton > button.clicked {
        background-color: rgb(200, 50, 100); /* Rouge après clic */
    }
    </style>
    """, unsafe_allow_html=True)

# JavaScript pour changer la classe du bouton au clic
st.markdown("""
    <script>
    // Fonction pour ajouter une classe au bouton lorsqu'il est cliqué
    document.addEventListener("DOMContentLoaded", function() {
        const btn = document.querySelector(".stButton > button");
        btn.addEventListener("click", function() {
            btn.classList.toggle("clicked");
        });
    });
    </script>
    """, unsafe_allow_html=True)

# Afficher le bouton avec fonctionnalité toggle
if st.button("Cliquez-moi !"):
    # Inverser l'état du bouton dans session_state
    st.session_state.button_clicked = not st.session_state.button_clicked

# Afficher ou masquer "Hello World" en fonction de l'état du bouton
if st.session_state.button_clicked:
    st.write("Hello World!")
