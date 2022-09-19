# Запуск через команду в консоль: streamlit run my.py
# Использовал PyCharm как IDE.
import io
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image

# components.html(
#     """
#     <link rel="stylesheet" href="static/style.css" type="text/css"/>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     <body style="start"></body>
#     """,
# )

st.markdown("""
<style>
start {
  padding-top: 80px;
}
</style>
""", unsafe_allow_html=True)

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