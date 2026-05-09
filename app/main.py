from fastapi import FastAPI

from app.db.database import engine
from app.models.log import Log
from app.db.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():

    return {
        "message": "Mega AI Multi-Agent System Running"
    }