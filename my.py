# Запуск через команду в консоль: streamlit run my.py
# Использовал PyCharm как IDE.
import io
import streamlit as st
from PIL import Image


def load_image():
    # Форма для загрузки изображения
    uploaded_file = st.file_uploader(
        label='Выберите изображение для нахождения мишек.')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице средствами Streamlit
        st.image(image_data)
        # Возврат изображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None

# Выводим заголовок страницы средствами Streamlit
st.title('Мишки! (Или кого мы там ищем.)')
# Вызываем функцию создания формы загрузки изображения
img = load_image()