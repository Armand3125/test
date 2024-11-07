import streamlit as st

pal = {
    "Noir Charbon": (0, 0, 0), "Blanc Jade": (255, 255, 255),
    "Jaune Or": (228, 189, 104), "Bleu Cyan": (0, 134, 214),
    "Violet Lila": (174, 150, 212), "Vert Gui": (63, 142, 67),
    "Rouge Ecarlate": (222, 67, 67), "Bleu Marine": (0, 120, 191),
    "Orange Mandarine": (249, 153, 99), "Vert Galaxie": (59, 102, 94),
    "Bleu Glacier": (163, 216, 225), "Violet Magenta": (236, 0, 140),
    "Gris Argent": (166, 169, 170), "Violet Basic": (94, 67, 183),
}

st.title("Sélection de Couleurs")

css = """
    <style>
        .stRadio label {
            color: black;
            font-weight: normal;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

cols = st.columns([1, 1, 1, 1])

with cols[0]:
    selected_color_1 = {}
    for color_name in pal.keys():
        selected_color_1[color_name] = st.checkbox("", key=color_name, value=False)

with cols[1]:
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

with cols[2]:
    selected_color_2 = {}
    for color_name in pal.keys():
        selected_color_2[color_name] = st.checkbox("", key=color_name, value=False)

with cols[3]:
    st.write("Couleurs disponibles :")
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

for color_name, selected in selected_color_1.items():
    if selected:
        rgb1 = pal[color_name]
        st.write(f"Vous avez sélectionné la couleur (ensemble 1) : {color_name}")
        st.markdown(
            f"<div style='background-color: rgb{rgb1}; width: 50px; height: 50px; border-radius: 5px;'></div>",
            unsafe_allow_html=True
        )

for color_name, selected in selected_color_2.items():
    if selected:
        rgb2 = pal[color_name]
        st.write(f"Vous avez sélectionné la couleur (ensemble 2) : {color_name}")
        st.markdown(
            f"<div style='background-color: rgb{rgb2}; width: 50px; height: 50px; border-radius: 5px;'></div>",
            unsafe_allow_html=True
        )
