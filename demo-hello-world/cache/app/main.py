import os
from typing import Dict
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def hello_world() -> Dict:
    return {"msg": "success", "text": "hello world"}
