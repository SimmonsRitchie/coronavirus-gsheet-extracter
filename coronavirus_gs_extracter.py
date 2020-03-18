
import logging
from dotenv import load_dotenv
from logs.config.logging import logs_config
from coronavirus_gs_extracter.download_sheet import download_sheet
from coronavirus_gs_extracter.copy_to_local import copy_to_local
from coronavirus_gs_extracter.copy_to_s3 import copy_to_s3
from coronavirus_gs_extracter.clean import clean_data

def main():

    # Load env vars
    load_dotenv()

    # Init logging
    logs_config()
    logging.info("Begin program")

    sheet_id = "2PACX-1vScoEuwTZAdLCbmWaoDsxRJcZSovzW-HI8UXlK7LqF-4FVr07pIARzCWoy0xjtlf0Wa5p1U0ZBEVnLQ"
    google_sheets = [
        {
            "name": "cases",
            "sheet_id": sheet_id,
            "gid": "0"
         },
        {
            "name": "deaths",
            "sheet_id": sheet_id,
            "gid": "1683428846"
        },
    ]

    # delete data from previous runs
    clean_data()

    for sheet in google_sheets:
        output_filename = f"{sheet['name']}.csv"
        download_sheet(sheet["name"], sheet["sheet_id"], sheet["gid"], output_filename)
        copy_to_s3(output_filename)
        copy_to_local(output_filename)


if __name__ == '__main__':
    main()