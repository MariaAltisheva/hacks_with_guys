import glob
import os
from typing import List, Tuple
# import docx
import pandas as pd
import easyocr


from pdf2image import convert_from_path
def get_file_properties(fp: str) -> Tuple[float, str, str]:
    """
    Возвращает описание файла
    :param fp: путь к файлу
    :return: размер, имя и расширение файла
    """
    split_tup = os.path.splitext(fp)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    file_stats = os.stat(fp)
    size = file_stats.st_size
    return size, file_name, file_extension


# def doc_text(fp: str) -> str:
#     """
#     конвертирует файл doc/docx в текст
#     :param fp: путь до конвертируемого файла
#     :return: текст
#     """
#     doc = docx.Document(fp)
#     full_text = []
#     for para in doc.paragraphs:
#         full_text.append(para.text)
#     return '\n'.join(full_text)
#
#
def pdf_text(fp: str, reader: easyocr.Reader) -> str:
    """
    конвертирует файл pdf в текст
    :param fp: путь до конвертируемого файла
    :param reader: вспомогательный файл из библиотеки easyocr
    :return: текст
    """
    images = convert_from_path(fp)
    full_text = []
    for image in images:
        image.save('buffer.jpg')
        result = reader.readtext('buffer.jpg', detail=0)
        full_text.append(' '.join(result))
    return '\n'.join(full_text)
