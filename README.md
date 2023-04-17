# Telegram Monitor

Telegram Monitor is a Python script that scans messages from all channels and groups in a Telegram account and sends a warning to a second Telegram account when specific keywords are detected.

## Prerequisites

- Python 3.7 or higher
- [Telethon](https://docs.telethon.dev/en/latest/) library

## Configuration

1. Create a new directory for the project and navigate to it in your terminal.
2. Clone or download the `telegram_monitor.py` and `schedule.sh` files into the project directory.
3. Install the Telethon library:


`usage`
```chmod +x schedule.sh```
```./schedule.sh```
The script will now monitor your Telegram account for messages containing the specified keywords and send a warning to your second Telegram account when a matching message is found.


