#!/usr/bin/env bash

# Cronjob script - this shell script is intended to be executed by a cronjob to run the program
# at regular intervals. If you're NOT setting up this program to run as a cronjob you can ignore this file and
# simply execute the program as described in the readme.

# If you do wish to set up a cronjob, you can adapt the paths in this script for your own purposes. Check docs/cronjob
# for more tips about setting up a cronjob.

# Start
echo "##############################"
echo $(date '+%Y-%m-%d %H:%M:%S')
echo "Script start - Google sheet extract and move"
# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# Run program
# Note: In this case executing path to binary due to problems with pyenv working in cron
~/.pyenv/versions/3.6.10/bin/pipenv run python coronavirus_gs_extracter.py
echo "Script end"