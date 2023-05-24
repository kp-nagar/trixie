from fastapi import FastAPI
from util.logger import logger
from services.trix_tts.trix_tts import TrixVoice


app = FastAPI()


@app.get("/")
def index():
    try:
        sound = TrixVoice().trix_in(text="hello how are you")
        logger.info(f"strime: {sound}")
        TrixVoice().trix_voice(sound)
        logger.info("said")
    except Exception as e:
            logger.error(e)
    return "Trixie is here."
