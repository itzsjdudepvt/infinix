from telethon import events
from .. import bot
import asyncio
import openai 
openai_key = "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"
#openai.api_key= openai_key

@bot.on(events.NewMessage(incoming=True, pattern= "(?i)/ask"))
async def _gpt(event): 
  if event.sender_id==int(1996525920): 
    await event.reply("Yess! You are My Developer You developed me very well")
  else: 
    await event.reply("You are User: Nice to meet you")