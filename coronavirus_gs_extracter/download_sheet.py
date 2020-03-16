import requests
from definitions import DIR_DATA
import logging


def download_sheet(sheet_name, sheet_id, gid):
    logging.info(f"Begin downloading sheet: {sheet_name}")
    s = requests.Session()
    google_sheet_url = f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?gid={gid}&single=true&output=csv"
    r = s.get(google_sheet_url)
    assert (r.status_code == 200), "Something went wrong with download"
    filename = f"{sheet_name}.csv"
    download_path = DIR_DATA/ filename
    with open(download_path, 'wb') as f:
        f.write(r.content)
        logging.info(f'{sheet_name} sheet downloaded as: {filename}')