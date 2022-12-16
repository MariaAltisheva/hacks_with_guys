import streamlit as st
from pathlib import Path
import base64

st.title("Demo")
# st.image(res, width = 800)

st.markdown("**Please fill the below form :**")
with st.form(key="Form :", clear_on_submit=True):
    File = st.file_uploader(label="Upload file", type=["pdf", "docx"])
    Submit = st.form_submit_button(label='Загрузить')


if Submit:
    st.markdown("**Файл успешно загружен**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = 'datas'
    save_path = Path(save_folder, File.name)
    with open(save_path, mode='wb') as w:
        w.write(File.getvalue())

    if save_path.exists():
        st.success(f'File {File.name} is successfully saved!')

