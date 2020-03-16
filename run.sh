#!/usr/bin/env bash
# Cronjob script

# Start
echo "New cronjob test"
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PYENV_VERSION=3.6.10
~/.pyenv/bin/pyenv versions
python --version
which python
# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# Run program
~/.pyenv/versions/3.6.10/bin/pipenv run python coronavirus_gs_extracter.py
# /home/dansr/.pyenv/shims/pipenv

#export PATH="/home/dansr/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"