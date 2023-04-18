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

# Load keywords configuration
with open('keywords.json', 'r') as keywords_file:
    keywords_config = json.load(keywords_file)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']
second_account_id = config['second_account_id']
keywords = keywords_config['keywords']

def check_keywords(text: str) -> bool:
    return any(keyword.lower() in text.lower() for keyword in keywords)

async def search_messages(client, entity):
    async for message in client.iter_messages(entity, limit=None):
        if check_keywords(message.text):
            await client.send_message(second_account_id, f"Warn: {message.text}")
            logging.info(f"Warn sent: {message.text}")

async def main():
    try:
        async with TelegramClient("anon", api_id, api_hash) as client:
            dialogs = await client(GetDialogsRequest(offset_date=None, limit=100))
            for dialog in dialogs.dialogs:
                entity = await client.get_entity(dialog.peer)
                await search_messages(client, entity)
        logging.info("Execution completed")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    logging.info("Starting telegram_monitor")
    asyncio.run(main())
