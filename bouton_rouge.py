import streamlit as st

st.session_state.setdefault("button_clicked", False)

st.title("Exemple de Bouton")
st.markdown("""
    <style>
    .stButton > button {
        color: black;
        background-color: rgb(200, 50, 100);
        padding: 20px 20px;
        font-size: 18px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button("Cliquez-moi !"):
    st.session_state.button_clicked = not st.session_state.button_clicked

if st.session_state.button_clicked:
    st.write("Hello World!")
