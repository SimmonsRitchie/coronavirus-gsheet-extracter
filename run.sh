#!/usr/bin/env bash
# Cronjob script

# Start
echo "New cronjob test"
~/.pyenv/bin/pyenv shell 3.6.10
~/.pyenv/bin/pyenv versions
whereis pipenv

## Set paths
#export PYENV_ROOT=~/.pyenv
#export PYENV_VERSION=3.6.10
#export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:"$PATH"
#export PATH=~/.pyenv/shims:~/.pyenv/bin:"$PATH"
#export PATH="${HOME}/.pyenv/scripts:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
#echo $PATH
#
## Searching
#pyenv versions
#whereis pyenv
#whereis pipenv
#python --version
## Start pyenv shell
#pyenv shell 3.6.10
## This tells pipenv to use this .env file
#export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
## Navigate to scraper project directory
#cd /home/dansr/projects/coronavirus_gs_extracter/
## Run program
#pipenv run python coronavirus_gs_extracter.py
