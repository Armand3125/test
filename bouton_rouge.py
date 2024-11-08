import streamlit as st

# Palette de couleurs
pal = {
    "NC": (0, 0, 0), "BJ": (255, 255, 255),
    "JO": (228, 189, 104), "BC": (0, 134, 214),
    "VL": (174, 150, 212), "VG": (63, 142, 67),
    "RE": (222, 67, 67), "BM": (0, 120, 191),
    "OM": (249, 153, 99), "VGa": (59, 102, 94),
    "BG": (163, 216, 225), "VM": (236, 0, 140),
    "GA": (166, 169, 170), "VB": (94, 67, 183),
}

st.title("Sélection de Couleurs")

# CSS pour aligner les rectangles et les cases à cocher sur la même ligne
css = """
    <style>
        /* Cacher les labels de boutons radio */
        .stRadio div [data-testid="stMarkdownContainer"] p {
            display: none;
        }
        /* Conteneur pour chaque couleur et case à cocher */
        .color-radio-container {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        /* Rectangle de couleur */
        .color-box {
            width: 50px;
            height: 20px;
            border-radius: 5px;
            margin-right: 10px;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Barre de sélection pour choisir le nombre de colonnes (entre 2 et 7)
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)

# Créer les colonnes en fonction de la sélection du slider
cols = st.columns(num_selections)  # Une colonne par sélection

# Options de couleurs disponibles
color_options = list(pal.keys())

# Afficher les sélecteurs de couleurs et les rectangles correspondants
for i in range(num_selections):
    with cols[i]:
        st.markdown("<div class='radio-container'>", unsafe_allow_html=True)
        
        # Afficher chaque couleur avec la case à cocher à droite
        for color_name, color_rgb in pal.items():
            # Utiliser une div pour aligner le rectangle et la case à cocher
            st.markdown(
                f"<div class='color-radio-container'>"
                f"<div class='color-box' style='background-color: rgb{color_rgb};'></div>"
                f"</div>",
                unsafe_allow_html=True
            )
        
        # Bouton radio pour sélectionner la couleur
        selected_color_name = st.radio("", color_options, key=f"radio_{i}")
        
        # Affichage de la couleur sélectionnée en grand rectangle
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.write(f"Vous avez sélectionné : {selected_color_name}")
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
                unsafe_allow_html=True
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
