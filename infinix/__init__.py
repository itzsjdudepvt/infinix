from telethon import TelegramClient
import logging
import time

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6010345930:AAHlgkmpiBe6nJ9--3zfLKXh_paGFc_1318"

bot = TelegramClient("cvotx", api_id, api_hash).start(bot_token = bot_token)

#bot1 = TelegramClient((StringSession()