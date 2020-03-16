
from coronavirus_gs_extracter.download_sheet import download_sheet
from coronavirus_gs_extracter.move_to_s3 import move_to_s3
from coronavirus_gs_extracter.clean import clean_data
def main():
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
        download_sheet(sheet["name"], sheet["sheet_id"], sheet["gid"])
        move_to_s3(sheet["name"])


if __name__ == '__main__':
    main()