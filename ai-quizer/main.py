from fastapi import FastAPI
import logging
from pydantic import BaseModel
from os import environ
from openai import OpenAI


logging.basicConfig(
    level=logging.INFO,
    filename='/var/log/app/quizer.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'
)
logger = logging.getLogger(__name__)



app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/test")
def get_test():
    logging.info("GET: Test endpoint called")
    return {"get test": "ok"}

@app.post("/test")
def post_test():
    logging.info("POST: Test endpoint called")
    return {"post test": "ok"}