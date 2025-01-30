#!/bin/bash
while true; do
    echo "Starting Discord bot..."
    python3 main.py
    echo "Bot crashed or stopped. Restarting in 5 seconds..."
    sleep 5
done
