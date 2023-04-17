import asyncio
import json
import logging
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest

# Setup logging
logging.basicConfig(filename='telegram_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']
second_account_id = config['second_account_id']

def check_keywords(text: str) -> bool:
    keywords = ["word1", "word2", "word3"]
    return any(keyword.lower() in text.lower() for keyword in keywords)

async def search_messages(client, entity):
    async for message in client.iter_messages(entity, limit=None):
        if check_keywords(message.text):
            await client.send_message(second_account_id, f"Warn: {message.text}")
            logging.info(f"Warn sent: {message.text}")

async def main():
    while True:
        try:
            async with TelegramClient("anon", api_id, api_hash) as client:
                dialogs = await client(GetDialogsRequest(offset_date=None, limit=100))
                for dialog in dialogs.dialogs:
                    entity = await client.get_entity(dialog.peer)
                    await search_messages(client, entity)
            logging.info("Waiting for next execution")
            await asyncio.sleep(3600)
        except Exception as e:
            logging.error(f"Error: {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    logging.info("Starting telegram_monitor")
    asyncio.run(main())
