import datetime
import os
from io import BytesIO
from gtts import gTTS   # TODO: research about another library
from pygame import mixer

from util.logger import logger


class TrixVoice:
    def trix_in(self, text, write_file=False, filename=None):
        # convert text to speech
        tts = gTTS(text=text, lang='en')
        logger.info(f"tts: {tts}")

        # check if input as byte stream
        if not write_file:
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            return mp3_fp

        # check if input as mp3 file
        if write_file:
            # if filename not exist filename=epoch_time
            if not filename:
                filename = f'{os.getcwd()}/records/{datetime.datetime.now().timestamp()}.mp3'
            tts.save(filename)
            return filename

    # play file/stream
    def trix_voice(self, tx):
        mixer.init()
        tx.seek(0)
        mixer.music.load(tx, "mp3")
        mixer.music.play()
