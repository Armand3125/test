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

# Affichage des options de couleur dans une radio
color_options = [f"{name}" for name in pal.keys()]
selected_color_name = st.radio("Choisissez une couleur", color_options)

# Afficher la couleur sélectionnée avec un carré de couleur
if selected_color_name:
    rgb = pal[selected_color_name]
    st.write(f"Vous avez sélectionné la couleur : {selected_color_name}")
    st.markdown(
        f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )
