from fastapi import FastAPI
from engine.db import init_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/state")
async def get_state():
    return {"status": "Updatopia engine online"}


