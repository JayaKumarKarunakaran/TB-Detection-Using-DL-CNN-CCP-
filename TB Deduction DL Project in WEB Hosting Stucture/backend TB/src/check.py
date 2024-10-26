from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request
app = FastAPI()
from utils import get_result



@app.get("/")
def hello():

    return {"message": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return get_result(image_file=file, is_api=True)
