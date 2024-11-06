import streamlit as st

# Définition de la palette de couleurs
pal = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

# Titre de l'application
st.title("Sélection de Couleurs")

# Afficher le sélecteur radio pour choisir une seule couleur
selected_color = st.radio(
    "Choisissez une couleur",
    options=list(pal.keys()),  # Liste des noms des couleurs
)

# Afficher la couleur sélectionnée et son apparence
if selected_color:
    rgb = pal[selected_color]
    st.write(f"Vous avez sélectionné la couleur : {selected_color}")
    st.markdown(f"<div style='background-color: rgb{rgb}; padding: 10px; margin-bottom: 5px;'> {selected_color} </div>", unsafe_allow_html=True)
