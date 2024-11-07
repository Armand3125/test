import streamlit as st

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

css = """
    <style>
        .stCheckbox label {
            color: black;
            font-weight: normal;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1])

# Utilisation des cases à cocher au lieu des boutons radio
selected_colors_1 = []
with cols[0]:
    for color_name in pal.keys():
        if st.checkbox(color_name, key=f"checkbox_1_{color_name}"):
            selected_colors_1.append(color_name)

with cols[1]:
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

selected_colors_2 = []
with cols[2]:
    for color_name in pal.keys():
        if st.checkbox(color_name, key=f"checkbox_2_{color_name}"):
            selected_colors_2.append(color_name)

with cols[3]:
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Répéter pour d'autres ensembles si nécessaire
# Afficher les couleurs sélectionnées
if selected_colors_1:
    st.write(f"Vous avez sélectionné ces couleurs pour l'ensemble 1 : {', '.join(selected_colors_1)}")
    
if selected_colors_2:
    st.write(f"Vous avez sélectionné ces couleurs pour l'ensemble 2 : {', '.join(selected_colors_2)}")
