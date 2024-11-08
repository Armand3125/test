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

# CSS pour aligner les rectangles et les cases à cocher horizontalement
css = """
    <style>
        /* Conteneur pour aligner chaque rectangle de couleur avec son bouton radio */
        .color-radio-row {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        /* Style du rectangle de couleur */
        .color-box {
            width: 50px;
            height: 20px;
            border-radius: 5px;
            margin-right: 10px;
        }
        /* Masquer les labels des boutons radio */
        .stRadio div [data-testid="stMarkdownContainer"] p {
            display: none;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Barre de sélection pour choisir le nombre de colonnes (entre 2 et 7)
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)

# Créer les colonnes en fonction de la sélection du slider
cols = st.columns(num_selections)

# Options de couleurs disponibles
color_options = list(pal.keys())

# Afficher les sélecteurs de couleurs et les rectangles correspondants
for i in range(num_selections):
    with cols[i]:
        # Titre pour chaque sélection de couleur
        st.markdown(f"<div class='radio-container'>", unsafe_allow_html=True)
        
        # Affichage des options avec les rectangles et les boutons radio
        selected_color_name = None
        for color_name, color_rgb in pal.items():
            # Aligner le rectangle et le bouton radio côte à côte
            st.markdown(
                f"<div class='color-radio-row'>"
                f"<div class='color-box' style='background-color: rgb{color_rgb};'></div>"
                f"{st.radio('', [color_name], key=f'{color_name}_{i}')}"
                f"</div>",
                unsafe_allow_html=True
            )

        # Si une couleur est sélectionnée, afficher le nom et un grand rectangle de la couleur
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.write(f"Vous avez sélectionné : {selected_color_name}")
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
                unsafe_allow_html=True
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
