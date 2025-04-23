import asyncio
from fastapi import FastAPI, BackgroundTasks
from util import botmessage,githubcommit

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(botmessage.fetchsendwebhook())


@app.get("/")
async def root(background_tasks: BackgroundTasks):
    background_tasks.add_task(lambda: None)
    return {"message": "Hello Worlddd"}

@app.get("/push/")
async def push_call():
    asyncio.create_task(botmessage.fetchsendwebhook())

@app.get("/commitlist/")
async def commitlist_call():
    repo_owner = "arbdoescode"
    repo_name = "Gitcord"

    raw_commits =  githubcommit.fetch_commits(repo_owner, repo_name)
    formatted_commits = githubcommit.format_commits(raw_commits)
    print(formatted_commits)
    return formatted_commits

