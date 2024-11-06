import streamlit as st
from sklearn.cluster import KMeans
from scipy.spatial import distance
from PIL import Image
import numpy as np

# Palette de couleurs définie
pal = {
    "Noir_Charbon": (0, 0, 0), "Blanc_Jade": (255, 255, 255),
    "Jaune_Or": (228, 189, 104), "Bleu_Cyan": (0, 134, 214),
    "Violet_Lila": (174, 150, 212), "Vert_Gui": (63, 142, 67),
    "Rouge_Ecarlate": (222, 67, 67), "Bleu_Marine": (0, 120, 191),
    "Orange_Mandarine": (249, 153, 99), "Vert_Galaxie": (59, 102, 94),
    "Bleu_Glacier": (163, 216, 225), "Violet_Magenta": (236, 0, 140),
    "Gris_Argent": (166, 169, 170), "Violet_Basic": (94, 67, 183),
}

# Calculer les couleurs les plus proches
def proches(c, pal):
    dists = [(n, distance.euclidean(c, col)) for n, col in pal.items()]
    return sorted(dists, key=lambda x: x[1])

def proches_lim(c, pal, n):
    return [n for n, _ in proches(c, pal)[:n]]

# Créer une nouvelle image en mappant les clusters aux couleurs de la palette
def nouvelle_img(img_arr, labels, cl_proches, selected_colors, pal):
    color_map = {i: pal[cl_proches[i][selected_colors[i]]] for i in range(len(cl_proches))}
    img_mapped = np.array([color_map[label] for label in labels])
    return img_mapped.reshape(img_arr.shape)

# Traiter l'image pour clustering et application de la palette
def traiter_img(img, Nc, Nd, dim_max):
    try:
        img = Image.open(img).convert('RGB')
        img.thumbnail((dim_max, dim_max))
        img_arr = np.array(img)

        pixels = img_arr.reshape(-1, 3)
        kmeans = KMeans(n_clusters=Nc, random_state=0).fit(pixels)
        labels = kmeans.labels_

        uniq, counts = np.unique(labels, return_counts=True)
        total_px = pixels.shape[0]
        cl_counts = dict(zip(uniq, counts))

        sorted_cls = sorted(cl_counts.items(), key=lambda x: x[1], reverse=True)
        cl_proches = [proches_lim(kmeans.cluster_centers_[i], pal, Nd) for i in cl_counts.keys()]

        if 'selected_colors' not in st.session_state:
            st.session_state.selected_colors = [0] * Nc
        elif len(st.session_state.selected_colors) != Nc:
            st.session_state.selected_colors = [0] * Nc

        new_img_arr = nouvelle_img(img_arr, labels, cl_proches, st.session_state.selected_colors, pal)
        st.session_state.modified_image = new_img_arr.astype('uint8')

        # Pour chaque couleur de la palette, on crée un bouton
        for color_name, color_rgb in pal.items():
            rgb_str = f"rgb({color_rgb[0]}, {color_rgb[1]}, {color_rgb[2]})"

            # Appliquer le style CSS au bouton avec la couleur de la palette
            button_style = f"""
            <style>
            .stButton > button {{
                color: white;
                background-color: {rgb_str};
                padding: 10px 20px;
                font-size: 18px;
                border-radius: 5px;
                width: 100%;
            }}
            </style>
            """
            st.markdown(button_style, unsafe_allow_html=True)

            # Créer le bouton pour chaque couleur avec son nom
            button_key = f'button_{color_name}'

            if st.button(label=color_name, key=button_key):
                # Action associée au bouton
                st.write(f"Vous avez sélectionné la couleur: {color_name}")
                # On peut ajouter une logique ici pour lier l'action à un autre processus
                # Par exemple, affecter la couleur sélectionnée à l'image traitée
                # (Cela peut être utile pour mettre à jour les couleurs du clustering, etc.)

    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

# Interface Streamlit
st.title("Tylice")
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
Nc = st.slider("Nombre de Clusters", 2, 7, 4)
Nd = st.slider("Nombre de Couleurs dans la Palette", 2, len(pal), 6)

# Fixer la dimension maximale de l'image à 400
dim_max = 400  

if uploaded_file is not None:
    traiter_img(uploaded_file, Nc, Nd, dim_max)

if 'modified_image' in st.session_state:
    st.image(st.session_state.modified_image, caption="Image Modifiée", width=int(1.5 * dim_max))
