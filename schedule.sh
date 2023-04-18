#!/bin/bash

# Check if the keywords config file exists, if not, create it
if [ ! -f "keywords.json" ]; then
    echo "Keywords config file not found. Creating a new one."

    # Prompt the user for the number of keywords
    echo "Enter the number of keywords you want to search for:"
    read num_keywords

    # Prompt the user for the keywords and save them in an array
    keywords=()
    for ((i=1; i<=$num_keywords; i++)); do
        echo "Enter keyword $i:"
        read keyword
        keywords+=("\"$keyword\"")
    done

    # Create the keywords.json file with the specified keywords
    echo "{" > keywords.json
    echo "  \"keywords\": [" >> keywords.json
    echo "    $(IFS=,; echo "${keywords[*]}")" >> keywords.json
    echo "  ]" >> keywords.json
    echo "}" >> keywords.json
fi

# Create a temporary crontab file
crontab -l > mycron.tmp

# Check if the script is already scheduled, if not, add the schedule
if ! grep -q "schedule.sh" mycron.tmp; then
    echo "0 * * * * /path/to/your/schedule.sh" >> mycron.tmp
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
