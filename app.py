from fastapi import FastAPI
from util.logger import logger
from services.trix_tts.trix_tts import TrixVoice


app = FastAPI()


@app.get("/")
def index():
    return "Trixie is here."

@app.get("/speak")
def speak(text: str):
    try:
        sound = TrixVoice().trix_in(text=text)
        logger.info(f"strime: {sound}")
        TrixVoice().trix_voice(sound)
        logger.info("speak task done.")
    except Exception as e:
        logger.error(e)
    return "Done"