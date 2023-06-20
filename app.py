from fastapi import FastAPI
import asyncio

from util.logger import logger
from services.trix_tts.trix_tts import TrixVoice, TrixTextVoice
from services.trix_tokenizer import TrixTokenizer
from services.trix_core import speak_trix


app = FastAPI()


@app.get("/")
def index():
    return "Trixie is here."


@app.get("/speak")
async def speak(text: str):
    try:
        logger.info("text: %s" % text)
        # texts = TrixTokenizer(text).texts
        # logger.info("total trix texts: %s" % len(texts))
        # tasks = [speak_trix(texts)]
        # await asyncio.gather(*tasks)
        sound = TrixTextVoice().trix_in(text=text)
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
