# SpeakApp
A web application in Flask that converts text to audio (TTS) using pyttsx3. It allows you to paste text or upload a .txt file, choose the system voice, and generate an MP3 file to listen to and download directly in your browser. All in a single Python script.
# Conversor de Texto para Áudio com Flask (Text-to-Speech)

Uma aplicação web simples, construída com Python e Flask, que converte texto em um arquivo de áudio MP3 que pode ser ouvido e baixado diretamente no navegador.

![Exemplo da Interface](https'://i.imgur.com/link-para-sua-imagem.png') <!--- Sugestão: tire um print da aplicação e hospede em um site como o imgur.com para colocar aqui --->

## 🚀 Sobre o Projeto

Este projeto foi criado para ser uma ferramenta online e de fácil acesso para a conversão de texto em fala (Text-to-Speech ou TTS). A aplicação utiliza a biblioteca `pyttsx3` para acessar as vozes de TTS instaladas no sistema operacional e o micro-framework Flask para criar a interface web.

Toda a lógica da aplicação, incluindo o backend, o HTML e o CSS, está contida em um único arquivo Python (`app.py`), tornando-o extremamente simples de executar e entender.

## ✨ Funcionalidades Principais

-   **Interface Web Amigável**: Interface limpa e responsiva criada com Bootstrap 5.
-   **Duas Formas de Entrada**: O usuário pode colar o texto em uma área de texto ou fazer o upload de um arquivo `.txt`.
-   **Seleção de Voz**: Lista e permite que o usuário escolha entre as diferentes vozes de TTS instaladas no sistema (incluindo diferentes idiomas).
-   **Geração de Áudio**: Converte o texto fornecido em um arquivo de áudio `.mp3`.
-   **Player Integrado**: Após a geração, um player de áudio aparece na tela para ouvir o resultado.
-   **Download Fácil**: Oferece um botão para baixar o arquivo de áudio gerado.

## 🛠️ Tecnologias Utilizadas

-   **Backend**:
    -   [Python 3](https://www.python.org/)
    -   [Flask](https://flask.palletsprojects.com/): Micro-framework web para criar a aplicação.
    -   [pyttsx3](https://pypi.org/project/pyttsx3/): Biblioteca para a síntese de fala.
-   **Frontend**:
    -   HTML5
    -   [Bootstrap 5](https://getbootstrap.com/): Framework CSS para estilização rápida.
    -   Jinja2: Motor de templates do Flask para renderizar o HTML dinamicamente.

## ⚙️ Como Executar

Siga os passos abaixo para rodar o projeto em sua máquina local.

**1. Pré-requisitos:**

-   Python 3 instalado.
-   `pip` (gerenciador de pacotes do Python).
-   Um motor de TTS instalado em seu sistema operacional (Windows, macOS e a maioria das distribuições Linux já possuem um por padrão).

**2. Clone o Repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**3. (Opcional, mas recomendado) Crie um Ambiente Virtual:**

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**4. Instale as Dependências:**

```bash
pip install Flask pyttsx3
```

**5. Execute a Aplicação:**

```bash
python nome_do_seu_script.py
```

**6. Acesse no Navegador:**

Abra seu navegador e acesse o endereço:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---
Feito com ❤️ por Enzo Hideki.
