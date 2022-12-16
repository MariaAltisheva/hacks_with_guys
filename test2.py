import streamlit as st


def load_file():
    """Загрузка title"""
    st.markdown("**Пожалуйста, загрузите документ в формате doc, jpg или pdf в данную форму:**")
    with st.form(key="Form :", clear_on_submit=True):
        File = st.file_uploader(label="Форма для распознавания документов в формате pdf, doc, jpeg, jpg, png",
                                type=["pdf", "docx", "jpeg", "jpg", "png"])
        Recognize = st.form_submit_button(label='Загрузить')
        return File, Recognize

