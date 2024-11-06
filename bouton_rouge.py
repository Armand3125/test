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

# Affichage des cases à cocher pour chaque couleur de la palette
selected_colors = []
for color_name, rgb in pal.items():
    if st.checkbox(color_name, key=color_name):
        selected_colors.append((color_name, rgb))

# Afficher les couleurs sélectionnées et leur apparence
if selected_colors:
    st.write("Vous avez sélectionné les couleurs suivantes :")
    for color_name, rgb in selected_colors:
        st.markdown(f"<div style='background-color: rgb{rgb}; padding: 10px; margin-bottom: 5px;'> {color_name} </div>", unsafe_allow_html=True)
else:
    st.write("Aucune couleur sélectionnée.")
