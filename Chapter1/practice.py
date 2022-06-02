from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["ROOT"])
async def first_api():
    return {'meaasge':  "Hello Nidhi, Welcome to the FAST API"}