import asyncio 
import discord 
from discord import Webhook, AllowedMentions
import aiohttp 
import os 

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(description="This is for employee of month <@881907187247636582> ")
        await webhook.send(
            embed=embed,
            username="Road Maintainer",
            allowed_mentions=AllowedMentions(users=True)
        )
        
if __name__ == "__main__":
    url = os.getenv("BOT_WEBHOOK")

    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()