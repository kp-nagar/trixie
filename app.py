from fastapi import FastAPI
from util.logger import logger


app = FastAPI()


@app.get("/")
def index():
    return "Trixie is here."
