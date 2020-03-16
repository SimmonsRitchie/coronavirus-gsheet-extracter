#!/bin/bash
# Cronjob script

# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/projects/dansr/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/projects/dansr/coronavirus_gs_extracter/
# This is needed to ensure pipenv runs when used from cron
PATH=/usr/local/bin:$PATH
# Run program
pipenv run python coronavirus_gs_extracter.py
