import streamlit as st

# Définition de la palette
pal = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

# Création des boutons pour chaque couleur
for color_name, rgb in pal.items():
    # Convertir RGB en code hexadécimal
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
    # Appliquer le style CSS au bouton
    st.markdown(f"""
        <style>
        .{color_name} > button {{
            background-color: {hex_color};
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            border: none;
        }}
        </style>
    """, unsafe_allow_html=True)
    # Créer le bouton avec le style défini
    if st.button(color_name, key=color_name):
        st.write(f"{color_name} activé !")
