import streamlit as st

# Définition de la palette de couleurs
pal = {
    "Noir Charbon": (0, 0, 0), "Blanc Jade": (255, 255, 255),
    "Jaune Or": (228, 189, 104), "Bleu Cyan": (0, 134, 214),
    "Violet Lila": (174, 150, 212), "Vert Gui": (63, 142, 67),
    "Rouge Ecarlate": (222, 67, 67), "Bleu Marine": (0, 120, 191),
    "Orange Mandarine": (249, 153, 99), "Vert Galaxie": (59, 102, 94),
    "Bleu Glacier": (163, 216, 225), "Violet Magenta": (236, 0, 140),
    "Gris Argent": (166, 169, 170), "Violet Basic": (94, 67, 183),
}

# Titre de l'application
st.title("Sélection de Couleurs")

# Création de 4 colonnes pour les systèmes de choix de couleur
cols = st.columns(4)

# Affichage de quatre systèmes de choix de couleur indépendants
for i, col in enumerate(cols):
    with col:
        # Affichage d'un radio bouton pour chaque colonne
        color_options = [f"{name}" for name in pal.keys()]
        selected_color_name = st.radio(f"Choisissez une couleur ({i+1})", color_options, key=f"color_select_{i}")

        # Afficher la couleur sélectionnée avec un carré de couleur
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.write(f"Vous avez sélectionné la couleur : {selected_color_name}")
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
                unsafe_allow_html=True
            )
