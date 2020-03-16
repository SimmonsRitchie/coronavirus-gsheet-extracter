#!/usr/bin/env bash
# Cronjob script

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
echo "Script end "