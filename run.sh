#!/usr/bin/env bash
# Cronjob script

# Start
echo "New cronjob test"
export PYENV_VERSION=3.6.10
~/.pyenv/bin/pyenv versions
python --version
# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# Run program
pipenv run python coronavirus_gs_extracter.py
