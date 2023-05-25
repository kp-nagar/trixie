from nltk import tokenize
from util.logger import logger


class TrixTokenizer:
    def __init__(self, text):
        logger.info("tokenizer executing")
        self.texts = tokenize.sent_tokenize(text)
