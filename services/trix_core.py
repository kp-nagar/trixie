from services.trix_tts.trix_tts import TrixTextVoice, TrixVoice
from util.logger import logger


async def speak_trix(texts):
    for i, tx in enumerate(texts):
        logger.info(f"trix voice: {i}")
        sound = TrixTextVoice().trix_in(text=tx)
        TrixVoice().trix_voice(sound)
    logger.info("all trix voice done.")
