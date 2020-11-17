import logging
import json
from dotenv import load_dotenv

from definitions import PATH_CONFIG_GSHEETS
from logs.config.logging import logs_config
from coronavirus_gs_extracter.download_sheet import download_sheet
from coronavirus_gs_extracter.copy_to_local import copy_to_local
from coronavirus_gs_extracter.copy_to_s3 import copy_to_s3
from coronavirus_gs_extracter.clean import clean_data
from time import sleep

def main():

    # Load env vars
    load_dotenv()

    # Init logging
    logs_config()
    logging.info("Begin program")

    # delete data from previous runs
    clean_data()

    # get google sheet config
    with open(PATH_CONFIG_GSHEETS) as f:
        config_sheets = json.load(f)

    for document in config_sheets:
        sheets = document.get("sheets", [])
        document_name = document.get("document_name")
        document_id = document.get("document_id")
        move_s3 = document.get("move_s3", False)
        bucket_name = document.get("bucket_name", None)
        bucket_dest_dir = document.get("bucket_dest_dir", None)
        move_local = document.get("move_local", False)
        logging.info(f"Extracting files from document: {document_name}")
        for sheet in sheets:
            sheet_name = sheet["name"]
            output_filename = f"{sheet_name}.csv"
            download_sheet(sheet_name, document_id, sheet["gid"], output_filename)
            if move_s3:
                if bucket_name and bucket_dest_dir:
                    copy_to_s3(output_filename, bucket_name, bucket_dest_dir)
                else:
                    raise ValueError('Missing bucket_name or bucket_dest_dir')
            if move_local:
                copy_to_local(output_filename)
            logging.info("Sleeping to avoid google rate limiting issues...")
            sleep(10)
            logging.info("Waking!")

if __name__ == "__main__":
    main()
