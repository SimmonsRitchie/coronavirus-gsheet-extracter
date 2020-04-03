### Coronavirus Google Sheet Extracter

Pulls data from targeted google sheets and uploads data as CSVs to specified AWS S3 accounts and/or local storage.

Rename config/gsheets-example.json as config/gsheets.json. Set document ID, individual sheet ID and other settings of
 your target sheets.

Rename .env.example as .env and insert your AWS credentials, bucket location and related settings.

### FAQ

#### How can I find the document ID and sheet ID for my google sheet?

From your google sheet, select: file > publish to the web

A modal will appear. Choose a sheet to publish as a CSV. The URL in the modal will change to something like:

    https://docs.google.com/spreadsheets/d/e/2PACX-1vScoEuwTZAdLCbmWaoDsxRJcZSovzW-HI8UXlK7LqF-4FVr07pIARzCWoy0xjtlf0Wa5p1U0ZBEVnLQ/pub?gid=0&single=true&output=csv

The document ID in this example is: "2PACX-1vScoEuwTZAdLCbmWaoDsxRJcZSovzW-HI8UXlK7LqF
-4FVr07pIARzCWoy0xjtlf0Wa5p1U0ZBEVnLQ"

The sheet ID is the value indicated by 'gid='. In this case it's "0"

#### Requirements

- Python 3.6

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
