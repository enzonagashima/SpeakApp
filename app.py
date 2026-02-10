from flask import Flask, render_template_string, request, send_file, redirect, url_for, flash
import pyttsx3
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "segredo_simples"

def get_voice_options():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Prepara opções de voz (exibe o nome e o idioma)
    options = []
    for voice in voices:
        lang = str(voice.languages[0]) if voice.languages else ""
        options.append({
            'id': voice.id,
            'name': voice.name,
            'lang': lang.replace("b'", '').replace("'", ''),
        })
    return options

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Conversor Texto para Áudio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {background: linear-gradient(120deg,#395886 0,#79bbff 100%); min-height: 100vh;}
        .card {margin-top: 80px; border-radius: 18px; box-shadow: 0 2px 8px #0001;}
        .form-label {font-weight: 500;}
        .footer {margin-top: 70px; color: #fff8; font-size: 0.9rem;}
        .navbar {border-radius:0 0 18px 18px;}
    </style>
</head>
<body>
<nav class="navbar navbar-dark bg-primary mb-4">
    <div class="container">
        <span class="navbar-brand mx-auto fs-4">Conversor de Texto para Áudio</span>
    </div>
</nav>
<div class="container d-flex justify-content-center">
    <div class="card p-4 col-md-8">
        <form method="POST" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="file" class="form-label">Selecione um arquivo .txt <b>ou</b> cole o texto abaixo:</label>
                <input class="form-control" type="file" name="file" id="file" accept=".txt">
            </div>
            <div class="mb-3">
                <textarea class="form-control" name="text" id="text" rows="8" placeholder="Cole ou digite seu texto aqui..."></textarea>
            </div>
            <div class="mb-3">
                <label for="voice" class="form-label">Escolha a voz:</label>
                <select class="form-select" name="voice" id="voice">
                {% for v in voices %}
                    <option value="{{v.id}}">{{v.name}} [{{v.lang}}]</option>
                {% endfor %}
                </select>
            </div>
            <button type="submit" class="btn btn-success w-100 fw-bold">Gerar Áudio</button>
        </form>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="alert alert-danger mt-3">{{ messages[0] }}</div>
        {% endif %}
        {% endwith %}
        {% if audio_url %}
            <div class="alert alert-success mt-4">
                <h5>Audio gerado!</h5>
                <audio controls src="{{ audio_url }}"></audio>
                <br>
                <a href="{{ audio_url }}" download="audio.mp3" class="btn btn-primary mt-2">Baixar Áudio</a>
            </div>
        {% endif %}
    </div>
</div>
<div class="text-center footer">
    Desenvolvido com amor usando Flask e pyttsx3 &middot; <small>Enzo Hideki (te amo Neite){{year}}</small>
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    audio_url = None
    voices = get_voice_options()
    if request.method == "POST":
        texto = ""
        f = request.files.get("file")
        if f and f.filename:
            if not f.filename.lower().endswith('.txt'):
                flash("Envie apenas arquivos .txt!")
                return render_template_string(HTML_TEMPLATE, audio_url=None, voices=voices, year=2024)
            safe_name = secure_filename(f.filename)
            texto = f.read().decode('utf-8')
        elif request.form.get("text"):
            texto = request.form.get("text")
        if not texto.strip():
            flash("Por favor, envie um arquivo ou cole algum texto!")
            return render_template_string(HTML_TEMPLATE, audio_url=None, voices=voices, year=2024)
        voice_id = request.form.get("voice")
        temp_dir = tempfile.gettempdir()
        temp_audio_path = os.path.join(temp_dir, f"audio_{os.getpid()}.mp3")
        engine = pyttsx3.init()
        # Seleciona voz
        if voice_id:
            engine.setProperty('voice', voice_id)
        engine.save_to_file(texto, temp_audio_path)
        engine.runAndWait()
        audio_url = url_for('audio', filename=os.path.basename(temp_audio_path))
        return render_template_string(HTML_TEMPLATE, audio_url=audio_url, voices=voices, year=2024)
    return render_template_string(HTML_TEMPLATE, audio_url=None, voices=voices, year=2024)

@app.route("/audio/<filename>")
def audio(filename):
    temp_dir = tempfile.gettempdir()
    temp_audio_path = os.path.join(temp_dir, filename)
    if os.path.exists(temp_audio_path):
        return send_file(temp_audio_path, mimetype="audio/mpeg", as_attachment=False, download_name="audio.mp3")
    else:
        flash("Áudio expirado ou não encontrado.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)