import asyncio
from fastapi import FastAPI, BackgroundTasks
from util import botmessage

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(botmessage.fetchsendwebhook())


@app.get("/")
async def root(background_tasks: BackgroundTasks):
    background_tasks.add_task(lambda: None)
    return {"message": "Hello Worlddd"}

@app.get("/push/")
async def other_call():
    asyncio.create_task(botmessage.fetchsendwebhook())

