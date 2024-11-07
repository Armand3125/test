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
        .stRadio label {
            color: black;
            font-weight: normal;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1])

# Colonne 1 : Couleur 1
with cols[0]:
    st.subheader("Couleur 1")  # Titre de la colonne
    color_options = [name for name in pal.keys()]
    selected_color_name_1 = st.radio("", color_options, key="radio_1")

# Colonne 2 : Couleur 2
with cols[1]:
    st.subheader("Couleur 2")  # Titre de la colonne
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Colonne 3 : Couleur 3
with cols[2]:
    st.subheader("Couleur 3")  # Titre de la colonne
    selected_color_name_2 = st.radio("", color_options, key="radio_2")

# Colonne 4 : Couleur 4
with cols[3]:
    st.subheader("Couleur 4")  # Titre de la colonne
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Colonne 5 : Couleur 5
with cols[4]:
    st.subheader("Couleur 5")  # Titre de la colonne
    selected_color_name_3 = st.radio("", color_options, key="radio_3")

# Colonne 6 : Couleur 6
with cols[5]:
    st.subheader("Couleur 6")  # Titre de la colonne
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Colonne 7 : Couleur 7
with cols[6]:
    st.subheader("Couleur 7")  # Titre de la colonne
    selected_color_name_4 = st.radio("", color_options, key="radio_4")

# Colonne 8 : Couleur 8
with cols[7]:
    st.subheader("Couleur 8")  # Titre de la colonne
    for color_name, color_rgb in pal.items():
        st.markdown(
            f"<div style='background-color: rgb{color_rgb}; width: 50px; height: 20px; border-radius: 5px; margin-bottom: 4px;'></div>",
            unsafe_allow_html=True
        )

# Affichage de la couleur sélectionnée pour chaque ensemble
if selected_color_name_1:
    rgb1 = pal[selected_color_name_1]
    st.write(f"Vous avez sélectionné la couleur (ensemble 1) : {selected_color_name_1}")
    st.markdown(
        f"<div style='background-color: rgb{rgb1}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )

if selected_color_name_2:
    rgb2 = pal[selected_color_name_2]
    st.write(f"Vous avez sélectionné la couleur (ensemble 2) : {selected_color_name_2}")
    st.markdown(
        f"<div style='background-color: rgb{rgb2}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )

if selected_color_name_3:
    rgb3 = pal[selected_color_name_3]
    st.write(f"Vous avez sélectionné la couleur (ensemble 3) : {selected_color_name_3}")
    st.markdown(
        f"<div style='background-color: rgb{rgb3}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )

if selected_color_name_4:
    rgb4 = pal[selected_color_name_4]
    st.write(f"Vous avez sélectionné la couleur (ensemble 4) : {selected_color_name_4}")
    st.markdown(
        f"<div style='background-color: rgb{rgb4}; width: 50px; height: 50px; border-radius: 5px;'></div>",
        unsafe_allow_html=True
    )
