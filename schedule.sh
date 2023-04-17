#!/bin/bash

# Create a temporary crontab file
crontab -l > mycron.tmp

# Check if the script is already scheduled, if not, add the schedule
if ! grep -q "run_telegram_monitor.sh" mycron.tmp; then
    echo "0 * * * * /path/to/your/run_telegram_monitor.sh" >> mycron.tmp
    crontab mycron.tmp
    echo "Cron job added"
else
    echo "Cron job already exists"
fi

# Remove the temporary file
rm mycron.tmp

# Activate your virtual environment if you have one (optional)
# source /path/to/your/virtualenv/bin/activate

# Run the Python script
python3 /path/to/your/telegram_monitor.py
