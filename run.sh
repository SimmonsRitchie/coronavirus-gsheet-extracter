# Cronjob script

# Start
echo "Start cronjob"
# Set paths
export PYENV_ROOT=~/.pyenv
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin
export PATH=~/.pyenv/shims:~/.pyenv/bin:"$PATH"

# Searching
whereis pyenv
whereis pipenv
python --version
# Start pyenv shell
pyenv shell 3.6.10
# This tells pipenv to use this .env file
export PIPENV_DOTENV_LOCATION="/home/dansr/projects/coronavirus_gs_extracter/.env"
# Navigate to scraper project directory
cd /home/dansr/projects/coronavirus_gs_extracter/
# Run program
pipenv run python coronavirus_gs_extracter.py
