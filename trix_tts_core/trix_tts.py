import datetime
import os
from io import BytesIO

from gtts import gTTS   # TODO: research about another library
import pygame


class TrixVoice:
    # initialize pygame for play audio
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def trix_in(self, text, write_file=False, filename=None):
        from app import app
        # convert text to speech
        tts = gTTS(text=text, lang=app.config['LANG'])

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
        pygame.mixer.music.load(tx, 'mp3')
        pygame.mixer.music.play()
        # this is stupid this if busy something.
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
