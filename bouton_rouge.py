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

# CSS pour masquer les labels et centrer les éléments
css = """
    <style>
        .stRadio label {
            display: none;
        }
        .radio-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 10px;
        }
        .color-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Barre de sélection pour choisir le nombre de colonnes (entre 2 et 7)
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)

# Créer les colonnes en fonction de la sélection du slider
cols = st.columns(num_selections * 2)  # On double le nombre pour inclure les couleurs

# Options de couleurs disponibles
color_options = list(pal.keys())

# Afficher les sélecteurs de couleurs et les rectangles correspondants
for i in range(num_selections):
    # Colonne pour le bouton radio de sélection de couleur sans texte
    with cols[i * 2]:
        with st.container():
            st.markdown("<div class='radio-container'>", unsafe_allow_html=True)
            selected_color_name = st.radio("", color_options, key=f"radio_{i}", label_visibility="collapsed")
            if selected_color_name:
                rgb = pal[selected_color_name]
                st.markdown(
                    f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
                    unsafe_allow_html=True
                )
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Colonne à côté pour afficher les rectangles de toutes les couleurs
    with cols[i * 2 + 1]:
        st.markdown("<div class='color-container'>", unsafe_allow_html=True)
        for color_name, color_rgb in pal.items():
            st.markdown(
                f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)
