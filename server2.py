# CFE Code - FastAPI
#https://github.com/tiangolo/fastapi
# uvicorn server2:fastApp
from fastapi import FastAPI

fastApp = FastAPI()

@fastApp.get("/fastApp")
async def root():
    return {"Dict_KEY": "Key Value"}