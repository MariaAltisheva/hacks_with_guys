import streamlit as st
from pathlib import Path

st.title("Загрузка документа для распознавания")
# st.image(res, width = 800)

st.markdown("**Please fill the below form :**")
with st.form(key="Form :", clear_on_submit=True):
    File = st.file_uploader(label="Upload file", type=["pdf", "docx"])
    Submit = st.form_submit_button(label='Submit')


if Submit:
    st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = 'F:/tmp'
    save_path = Path(save_folder, File.name)
    with open(save_path, mode='wb') as w:
        w.write(File.getvalue())

    if save_path.exists():
        st.success(f'File {File.name} is successfully saved!')
