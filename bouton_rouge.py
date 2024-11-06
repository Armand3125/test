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

# Créer une liste de labels personnalisés pour le radio, avec des rectangles colorés
color_options = [
    f"<div style='background-color: rgb{rgb}; width: 30px; height: 30px; display: inline-block; margin-right: 10px;'></div>{color_name}"
    for color_name, rgb in pal.items()
]

# Afficher le sélecteur radio avec des rectangles colorés
selected_color = st.radio(
    "Choisissez une couleur",
    options=color_options,
    format_func=lambda x: ""  # Cette ligne permet de ne pas afficher le texte de l'option, juste le rectangle
)

# Extraire le nom de la couleur à partir de la sélection
selected_color_name = next(color_name for color_name, rgb in pal.items() if f"<div style='background-color: rgb{rgb}" in selected_color)

# Afficher la couleur sélectionnée et son apparence
if selected_color:
    rgb = pal[selected_color_name]
    st.write(f"Vous avez sélectionné la couleur : {selected_color_name}")
    st.markdown(f"<div style='background-color: rgb{rgb}; padding: 10px; margin-bottom: 5px;'> </div>", unsafe_allow_html=True)
