import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_DIR = BASE_DIR / "ideas_for_test" / "work_with_csv"
OUTPUT_CSV = Path(__file__).resolve().parent / "result_Fon.csv"

JSON_DIR = BASE_DIR / "ideas_for_test" / "work_with_json"
JSON_LOG = Path(__file__).resolve().parent / "json__Fon.log"

XML_FILE = BASE_DIR / "ideas_for_test" / "work_with_xml" / "groups.xml"


def read_csv_file(file_path, delimiter):
    with file_path.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.reader(file, delimiter=delimiter)

        header = next(reader)

        if header and header[-1] == "":
            header.pop()

        rows = []

        for row in reader:
            row = row[:len(header)]
            rows.append(row)

    return header, rows


def remove_csv_duplicates():
    header, random_rows = read_csv_file(
        CSV_DIR / "random.csv", ","
    )

    rmc_header, rmc_rows = read_csv_file(
        CSV_DIR / "rmc.csv", ";"
    )

    if header != rmc_header:
        raise ValueError("CSV files have different headers")

    all_rows = random_rows + rmc_rows
    unique_records = {}

    for row in all_rows:
        key = (row[0], row[15], row[16], row[17])
        unique_records.setdefault(key, row)

    with OUTPUT_CSV.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(unique_records.values())

    print(f"Total records: {len(all_rows)}")
    print(f"Unique records: {len(unique_records)}")
    print(f"Result saved to: {OUTPUT_CSV}")


def validate_json_files():
    logging.basicConfig(
        filename=JSON_LOG,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w",
        force=True,
    )

    json_files = list(JSON_DIR.glob("*.json"))

    for file_path in json_files:
        try:
            with file_path.open("r", encoding="utf-8") as file:
                json.load(file)

        except json.JSONDecodeError as error:
            logging.error(
                "Invalid JSON file %s: %s",
                file_path.name,
                error,
            )

        except OSError as error:
            logging.error(
                "Cannot read file %s: %s",
                file_path.name,
                error,
            )

    print(f"JSON files checked: {len(json_files)}")
    print(f"Error log: {JSON_LOG}")


xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)
xml_logger.propagate = False

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter("%(levelname)s - %(message)s")
)
xml_logger.addHandler(console_handler)


def find_incoming_by_group_number(group_number):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.findtext("number")

        if number == str(group_number):
            return group.findtext("timingExbytes/incoming")

    return None



if __name__ == "__main__":
    remove_csv_duplicates()
    validate_json_files()

    group_number = 0
    incoming = find_incoming_by_group_number(group_number)

    if incoming is not None:
        xml_logger.info(
            "Group %s: incoming = %s",
            group_number,
            incoming,
        )
    else:
        xml_logger.info(
            "Group %s: incoming not found",
            group_number,
        )

