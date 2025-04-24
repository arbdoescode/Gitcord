import asyncio
from fastapi import FastAPI, BackgroundTasks
from util import botmessage,githubcommit
from model import webhookreq
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(botmessage.fetchsendmsg("Api Deployed Succesfully"))
    return {"message": "Hello Worlddd"}



@app.get("/")
async def root(background_tasks: BackgroundTasks):
    background_tasks.add_task(lambda: None)
    return {"message": "Hello Worlddd"}

@app.get("/push/")
async def push_call():
    asyncio.create_task(botmessage.fetchsendmsg("Test push"))

@app.get("/commitlist/")
async def commitlist_call():
    repo_owner = "arbdoescode"
    repo_name = "Gitcord"

    raw_commits =  githubcommit.fetch_commits(repo_owner, repo_name)
    formatted_commits = githubcommit.format_commits(raw_commits)
    print(formatted_commits)
    return formatted_commits

@app.post("/botpushreminder/")
async def botpushreminde_call(item: webhookreq.PushWebhook):
    asyncio.create_task(botmessage.fetchsendwebhook(item))
    return item
