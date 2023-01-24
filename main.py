from http.client import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import aiofiles

from fastapi import FastAPI

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados")
async def read_dates():
    try:
        async with aiofiles.open("dates.json", mode="r") as f:
            content = await f.read()
            return json.loads(content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

# uvicorn main:app --host ***.**.**.*** --port 80