import os
import json
import logging


def validate_json_files(folder_path):
    log_file = "json_davydyak.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    files = os.listdir(folder_path)

    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(folder_path, file)

            try:
                with open(file_path, "r", encoding="utf-8") as json_file:
                    json.load(json_file)

                print(f"{file} is valid")

            except json.JSONDecodeError as error:
                logging.error(f"{file} is invalid JSON: {error}")
                print(f"{file} is invalid")


if __name__ == "__main__":
    folder_path = "ideas_for_test/work_with_json"
    validate_json_files(folder_path)