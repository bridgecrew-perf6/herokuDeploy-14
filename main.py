from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


class Radio(BaseModel):
    sex: str

api = FastAPI()

origins = ["http://localhost", "http://localhost:8080"]
api.add_middleware(CORSMiddleware, allow_origins=["*"],
allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@api.post("/radio")
def probar(uno: Radio):
    print(uno)
    return uno