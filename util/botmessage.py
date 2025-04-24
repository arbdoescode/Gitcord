import asyncio 
import discord 
from discord import Webhook, AllowedMentions
import aiohttp 
import ast
import os 
from dotenv import load_dotenv
from datetime import datetime
from model import webhookreq

async def sendSimpleMessage(url,msg):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(description=msg)
        await webhook.send(
            embed=embed,
            username="Road Maintainer",
            allowed_mentions=AllowedMentions(users=True)
        )

async def sendPushMessage(url, author, project_path, commit_message, timestamp_str, commit_hash, commit_url):
    dt = datetime.fromisoformat(timestamp_str)
    unix_timestamp = int(dt.timestamp())

    message = (
        f"<@{author}> committed a push on **\"{project_path}\"**\n"
        f"Message: **\"{commit_message}\"**\n"
        f"Timestamp: <t:{unix_timestamp}:F>\n"
        f"__[{commit_hash[:7]}]({commit_url})__"

    )

    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(description=message)
        await webhook.send(
            embed=embed,
            username="Road Maintainer",
            allowed_mentions=AllowedMentions(users=True)
        )

async def fetchsendmsg(msg):
    load_dotenv()
    url = os.getenv("BOT_WEBHOOK")

    if not url:
        raise RuntimeError("BOT_WEBHOOK environment variable is not set.")
    
    await sendSimpleMessage(url, msg)

async def fetchsendwebhook(item: webhookreq.PushWebhook):
    load_dotenv()
    url = os.getenv("BOT_WEBHOOK")

    user_test_raw = os.getenv("USER_TEST")
    user_test = ast.literal_eval(user_test_raw)  
    user_dict = {name: id_num for name, id_num in user_test}
    query = item.pusher.name
    pushername = item.pusher.name
    if query in user_dict:
        pushername=user_dict[query]
    else:
        print(f"{query} not found")

    if not url:
        raise RuntimeError("BOT_WEBHOOK environment variable is not set.")
    
    await sendPushMessage(url, pushername,item.repository.full_name,item.head_commit.message,item.head_commit.timestamp,item.after,item.head_commit.url)

