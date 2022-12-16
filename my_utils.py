import base64

import streamlit as st
from pathlib import Path




def start():
# Настройка заголовка и текста
    st.title("Хакатон X-Mas Hacks")
    st.write("""Определение вида договора с интерпретацией результатов.""")
    st.write("""Проект разработан командой участников: Акопян Артем, Алтышева Мария, Наумов Константин""")

    # Настройка боковой панели
    st.sidebar.title("Крисмас-тим")

    st.title("Загрузка документа для распознавания")
    # st.image(res, width = 800)

def load_file():
    """Загрузка title"""
    st.markdown("**Пожалуйста, загрузите документ в формате doc, jpg или pdf в данную форму:**")
    with st.form(key="Form :", clear_on_submit=True):
        File = st.file_uploader(label="Форма для распознавания документов в формате pdf, doc, jpeg, jpg, png",
                                type=["pdf", "docx", "jpeg", "jpg", "png"])
        Recognize = st.form_submit_button(label='Загрузить')
        return File, Recognize

def buttom_push(File):
    """Загрузка формы подгрузки документа, на выходе получаем сам файл и булево знаение, нажата ли кнопка"""
    st.markdown("**Файл успешно загружен**")
    # save_folder = 'datas'
    # save_path = Path(save_folder, File.name)
    # with open(save_path, mode='wb') as w:
    #     w.write(File.getvalue())
    # if save_path.exists():
    #     st.success(f'Файл {File.name} успешно загружен')


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )





