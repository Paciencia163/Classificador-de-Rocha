## Classificador de Rochas 

Este projeto consiste em uma aplicação Streamlit que classifica imagens de rochas usando um modelo de aprendizado de máquina treinado com o conjunto de dados "Rock Classification" disponível no Kaggle: [https://www.kaggle.com/datasets/salmaneunus/rock-classification](https://www.kaggle.com/datasets/salmaneunus/rock-classification).

### Funcionalidades

* **Upload de Imagem:** A aplicação permite que você carregue uma imagem de uma rocha.
* **Classificação:** O modelo treinado classifica a rocha na imagem e exibe o tipo de rocha previsto.
* **Interface Simples:** A aplicação tem uma interface simples e fácil de usar, criada com o Streamlit.

### Instalação

1. **Clone este repositório:**
```bash
git clone https://github.com/seu-usuario/classificador-de-rochas.git
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate   # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
streamlit run ClassificarRochas.py
```

### Uso

1. Execute a aplicação Streamlit (verifique a seção "Instalação").
2. Clique no botão "Carregue uma imagem de uma rocha" e selecione a imagem que deseja classificar.
3. A aplicação mostrará a imagem carregada e o tipo de rocha previsto.

### Notas

* O modelo de aprendizado de máquina foi treinado usando o conjunto de dados "Rock Classification" disponível no Kaggle. 
* A aplicação pode ser aprimorada com a adição de recursos como:
    * Visualização da matriz de confusão do modelo.
    * Exibição das probabilidades de cada classe.
    * Possibilidade de salvar a classificação da imagem.

### Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir um pull request com suas melhorias ou correções.

### Licença

Este projeto é licenciado sob a licença [MIT](LICENSE). 
