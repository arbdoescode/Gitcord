import asyncio 
import discord 
from discord import Webhook, AllowedMentions
import aiohttp 
import os 
from dotenv import load_dotenv


async def sendSimpleMessage(url,msg):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(description=msg)
        await webhook.send(
            embed=embed,
            username="Road Maintainer",
            allowed_mentions=AllowedMentions(users=True)
        )

async def fetchsendwebhook():
    load_dotenv()
    url = os.getenv("BOT_WEBHOOK")

    if not url:
        raise RuntimeError("BOT_WEBHOOK environment variable is not set.")
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(sendSimpleMessage(url,"test"))
    loop.close()