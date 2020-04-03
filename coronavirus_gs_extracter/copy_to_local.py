import logging
import os
from definitions import DIR_DATA
from pathlib import Path
import shutil


def copy_to_local(filename):
    local_file_path = DIR_DATA / filename
    local_destination_dir = os.environ.get("LOCAL_DESTINATION_DIR")

    if local_destination_dir:
        logging.info(f"Copying file to local destination: {local_destination_dir}")
    else:
        logging.info(
            "LOCAL_DESTINATION_DIR env var not set - file will not be copied to a local destination "
        )
        return

    local_destination_dir = Path(local_destination_dir)
    if local_destination_dir.is_dir():
        shutil.copy(str(local_file_path), str(local_destination_dir))
        logging.info("File copied to destination")
    else:
        logging.error("Local destination directory doesn't exist - abort")
        return
