import base64
import io
from io import StringIO

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json
from PIL import Image


# Настройка заголовка и текста
st.title("Хакатон X-Mas Hacks")
st.write("""Определение вида договора с интерпретацией результатов.""")
st.write("""Проект разработан командой участников: Акопян Артем, Алтышева Мария, Наумов Константин""")

# Настройка боковой панели
st.sidebar.title("Крисмас-тим")

def load_image():
    """Создание формы для загрузки изображения"""
    upload_file = st.file_uploader(label='Выберите изображение для распознавания')
    if upload_file is not None:
        image_data = upload_file.getvalue()
        # Показ загруженного изображения
        st.image(image_data)
        # Возврат ихображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None

# форма загрузки изображения
img = load_image()


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

add_bg_from_local('light.png')
