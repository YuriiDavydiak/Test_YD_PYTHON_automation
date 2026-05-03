import xml.etree.ElementTree as ET
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_incoming_by_group(file_path, group_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    groups = root.findall("group")

    for group in groups:
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                logging.info(
                    f"group {group_number}: incoming = {incoming.text}"
                )
                return incoming.text

    logging.info(f"group {group_number} not found")
    return None


if __name__ == "__main__":
    file_path = "ideas_for_test/work_with_xml/groups.xml"
    find_incoming_by_group(file_path, 5)