#!/bin/bash
# Cronjob script

# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# This is needed to ensure pipenv runs when used from cron
export PYENV_VERSION="3.6.10"
export PATH=~/.pyenv/shims:~/.pyenv/bin:"$PATH"
# Run program
pipenv run python coronavirus_gs_extracter.py
