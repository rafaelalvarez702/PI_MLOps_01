


#librerías
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
