from fastapi import FastAPI
from util.logger import logger
from services.trix_tts.trix_tts import TrixTextVoice, TrixVoice


app = FastAPI()


@app.get("/")
def index():
    return "Trixie is here."

@app.get("/speak")
def speak(text: str):
    try:
        logger.info("text: %s" % text)
        sound = TrixTextVoice().trix_in(text=text)
        logger.info(f"stream: {sound}")
        TrixVoice().trix_voice(sound)
        logger.info("speak task done.")
    except Exception as e:
        logger.error(e)
    return "Done"

@app.get("/stop")
def stop_speak():
    try:
        TrixVoice().trix_voice_stop()
        logger.info("stop speak task done.")
    except Exception as e:
        logger.error(e)
    return "Done"

@app.get("/speaking")
def check_speaking():
    try:
        speaking = TrixVoice().trix_speaking()
        logger.info("stop speak task done.")
    except Exception as e:
        logger.error(e)
    return speaking