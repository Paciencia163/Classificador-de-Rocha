import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Carregue o modelo salvo uma única vez
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('modelo_de_classificacao_de_rochas.h5')

# Lista de classes
CLASS_NAMES = ['Basalt', 'Granite', 'Marble', 'Quartzite', 'Coal', 'Sandstone', 'Limestone']

# Função de pré-processamento da imagem
def preprocess_image(image):
    image = image.resize((224, 224))  # Redimensionando a imagem
    image_array = np.array(image)  # Convertendo para array NumPy
    image_array = image_array / 255.0  # Normalização
    image_array = np.expand_dims(image_array, axis=0)  # Expandindo dimensões
    return image_array

# Função de classificação
def classify_image(model, processed_image):
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)
    return CLASS_NAMES[predicted_class]

# Página Inicial
def main_page(model):
    st.title('Sistema Inteligente Classificador de Rochas - Utilizando Deep Learning')
    
    # Exibir uma imagem na página inicial
    st.image("rochas_inicial.jpg", caption="Bem-vindo ao Classificador de Rochas", use_column_width=True)
    
    # Selecione a fonte da imagem
    option = st.selectbox("Escolha a fonte da imagem:", ("Capturar com Câmera", "Carregar do Dispositivo"))

    image = None

    if option == "Capturar com Câmera":
        camera_image = st.camera_input("Tire uma foto da rocha")
        if camera_image is not None:
            image = Image.open(camera_image)

    elif option == "Carregar do Dispositivo":
        uploaded_file = st.file_uploader("Carregue uma imagem de uma rocha", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)

    if image is not None:
        st.image(image, caption='Imagem carregada', use_column_width=True)

        # Pré-processar e classificar a imagem
        processed_image = preprocess_image(image)
        prediction = classify_image(model, processed_image)

        # Exiba a previsão
        st.write(f'A imagem provavelmente é uma **{prediction}**')
    else:
        st.write("Por favor, forneça uma imagem para classificação.")

# Página Tipos de Rochas
def rock_types_page():
    st.title('Tipos de Rochas')

    rock_info = {
        "Basalt": "O basalto é uma rocha ígnea de granulação fina e de cor escura.",
        "Granite": "O granito é uma rocha ígnea de granulação média a grossa, composta principalmente por quartzo, feldspato e mica.",
        "Marble": "O mármore é uma rocha metamórfica composta principalmente de calcita.",
        "Quartzite": "O quartzito é uma rocha metamórfica formada a partir do arenito rico em quartzo.",
        "Coal": "O carvão é uma rocha sedimentar formada a partir da matéria vegetal que foi comprimida e endurecida ao longo do tempo.",
        "Sandstone": "O arenito é uma rocha sedimentar composta principalmente de partículas de areia compactadas.",
        "Limestone": "O calcário é uma rocha sedimentar composta principalmente de carbonato de cálcio."
    }

    for rock, description in rock_info.items():
        st.subheader(rock)
        st.image(f"{rock.lower()}.jpg", caption=rock, use_column_width=True)
        st.write(description)

# Página de Contato
def contact_page():
    st.title('Contacto do Desenvolvedor')
    st.write("Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contacto:")
    st.write("**Nome:** Paciência Aníbal Muienga")
    st.write("**Email:** paciencia163@gmail.com")
    st.write("**LinkedIn:** [linkedin.com/in/pacienciaanibalmuienga](https://linkedin.com/in/paciencia)")

# Carregar o modelo fora de qualquer função, garantindo que ele esteja disponível
model = load_model()

# Navegação
page = st.sidebar.selectbox("Navegação", ["Página Inicial", "Tipos de Rochas", "Contacto"])

if page == "Página Inicial":
    main_page(model)
elif page == "Tipos de Rochas":
    rock_types_page()
elif page == "Contacto":
    contact_page()
