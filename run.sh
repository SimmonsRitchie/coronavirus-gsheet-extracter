#!/usr/bin/env bash
# Cronjob script

# Start
echo "Cronjob run - Google sheet extract and move"
echo $(date '+%Y-%m-%d %H:%M:%S')
# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# Run program
~/.pyenv/versions/3.6.10/bin/pipenv run python coronavirus_gs_extracter.py
