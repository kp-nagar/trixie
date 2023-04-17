from logger.logger import logger
from flask import Flask, Blueprint
from views.views import register_urls_in_blueprint

app = Flask(__name__)


# Config
app.config.from_object('config.config')


# for blueprint url
trix_blueprint = Blueprint('auth', __name__)
register_urls_in_blueprint(trix_blueprint)
app.register_blueprint(trix_blueprint)


@app.route("/")
def index():
    return "<p>Welcome to Trixie TTS!</p>"


@app.route("/voice")
def test_trix_voice():
    from trix_tts_core.trix_tts import TrixVoice
    tx = TrixVoice().trix_in("your test is successful without file.")
    TrixVoice().trix_voice(tx)
    return "Test successful"


@app.route("/file")
def test_trix_voice_file():
    from trix_tts_core.trix_tts import TrixVoice
    tx = TrixVoice().trix_in("your test is successful with file.", write_file=True)
    TrixVoice().trix_voice(tx)
    return f"Test successful with file {tx}."


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7001, passthrough_errors=False, debug=True)
