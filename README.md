### Coronavirus Google Sheet Extracter

Pulls data from targeted google sheets and uploads data as CSVs to specified AWS S3 accounts and/or local storage.

Set document ID, individual sheet ID and other settings of your target sheets in config/gsheets.json. See gsheets
-example.json for an example of a config file.

Rename .env.example as .env and insert your AWS credentials, bucket location and related settings.

#### Requirements

- Python 3.6+

#### Install

1. Open the terminal. Clone the project repo

    `git clone https://github.com/SimmonsRitchie/coronavirus_gs_extracter.git`

2. If you don't have pipenv installed on your machine, run:

    `pip install pipenv`

3. Navigate into the project directory:

    `cd coronavirus_gs_extracter`
     
4. Use pipenv to create a virtual environment and install the project 
dependencies. Run:

    `pipenv install`

5. Copy .env.example and rename .env

    `cp .env.example .env`

6. Enter your AWS S3 credentials and other settings into .env

#### Run

From the terminal, make sure you're in the project directory. Run the following:

```python coronavirus_gs_extracter.py```

Or:

```pipenv run python coronavirus_gs_extracter.py```
