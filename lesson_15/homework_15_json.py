import os
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="json_davydiak.log",
    filemode="w"
)
folder_path = "ideas_for_test/work_with_json"

for file_name in os.listdir(folder_path):

    if file_name.endswith(".json"):

        full_path = os.path.join(folder_path, file_name)

        try:
            with open(full_path, "r", encoding="utf-8") as file:
                json.load(file)

            logging.info(f"{file_name} is valid JSON")

        except json.JSONDecodeError as error:
            logging.error(f"{file_name} is INVALID JSON -> {error}")

        except Exception as error:
            logging.error(f"{file_name} unexpected error -> {error}")