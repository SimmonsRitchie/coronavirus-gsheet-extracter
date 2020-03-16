import logging
import boto3
import os
from definitions import DIR_DATA


def move_to_s3(sheet_name):
    logging.info(f"Move {sheet_name} to s3")
    local_file_path = DIR_DATA / f"{sheet_name}.csv"

    try:
        # CHECK JSON PAYLOAD EXISTS
        if not local_file_path.is_file():
            logging.error(f"No file found at {local_file_path},"
            "aborting attempt to move file to S3.")
            raise

        # GET ENV VARS
        bucket_name = os.environ.get("BUCKET_NAME")
        keyID = os.environ.get("KEY_ID")
        sKeyID = os.environ.get("SECRET_KEY_ID")
        source_path = str(local_file_path.resolve())
        destination_path = os.environ.get("DESTINATION_PATH")

        # LOGGING
        logging.info(f"Moving {source_path} to S3 bucket {bucket_name}...")
        logging.info(f"File will be saved in: {destination_path}")

        # CONNECT TO S3
        session = boto3.Session(
            aws_access_key_id=keyID,
            aws_secret_access_key=sKeyID,
        )
        s3 = session.resource('s3')

        # UPLOAD
        s3.Bucket(bucket_name).upload_file(source_path, destination_path)
        logging.info(f"file uploaded to {destination_path}")
    except Exception as e:
        logging.error("Something went wrong when attempting to copy file" \
                        " to S3 bucket")
        logging.exception(e)
        return

