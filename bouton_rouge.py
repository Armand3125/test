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

# Slider for number of color selections
num_selections = st.slider("Nombre de sélections de couleur", min_value=2, max_value=7, value=4)

# Create columns dynamically based on slider value
cols = st.columns(num_selections)

color_options = [name for name in pal.keys()]

for i in range(num_selections):
    with cols[i]:
        selected_color_name = st.radio("", color_options, key=f"radio_{i}")
        if selected_color_name:
            rgb = pal[selected_color_name]
            st.markdown(
                f"<div style='background-color: rgb{rgb}; width: 50px; height: 50px; border-radius: 5px;'></div>",
                unsafe_allow_html=True
            )
            st.write(f"Vous avez sélectionné la couleur (ensemble {i + 1}) : {selected_color_name}")
