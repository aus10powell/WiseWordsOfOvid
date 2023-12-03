#!/bin/bash
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

# Set the timezone to PST
export TZ="America/Los_Angeles"

# Format the current date and time
current_datetime=$(date +"%Y-%m-%d_%H-%M-%S")

# Create a text file with the formatted date and time
text_file="job_run_at_${current_datetime}.txt"

# Example path
echo "Hello, this is a sample text file created at ${current_datetime} in PST." > "/root/OvidQuotes/job_logs/${text_file}"

# Execute bot
/root/OvidQuotes/venv/bin/python /root/OvidQuotes/app/bot.py 