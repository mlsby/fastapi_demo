from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    input_text: str

pipe = {}
app = FastAPI()

@app.on_event("startup")
async def load_model():
    pipe['toxic'] = pipeline('text-classification', model='unitary/toxic-bert')

@app.get("/")
async def root():
    return {"message": "Toxicity classifyer"}

@app.post("/predict")
async def predict(item: Item):
    """calssifies input text as toxic or not"""
    if 'toxic' in pipe.keys():
        score = pipe['toxic'](item.input_text)[0]['score']
        return {'toxic': score > 0.5}
    else:
        return {'message': 'no pipe'}

