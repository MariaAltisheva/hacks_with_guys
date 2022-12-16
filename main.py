import streamlit as st


from my_utils import start, load_file, buttom_push, add_bg_from_local, get_file_properties, docx_text

# Загрузка title и темы
start()
add_bg_from_local('light.png')

# Загрузка формы подгрузки документа, на выходе получаем сам файл и булево знаение, нажата ли кнопка
File, Recognize = load_file()

if Recognize:
    if File is None:
        st.markdown("**Вы ничего не загрузили**")
    else:
        buttom_push(File)


st.write(docx_text(f'{File.name}'))

