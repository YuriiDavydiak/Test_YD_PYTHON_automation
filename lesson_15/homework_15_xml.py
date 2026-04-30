import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_incoming_by_group_number(group_number):
    file_path = "ideas_for_test/work_with_xml/groups.xml"

    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall(".//group"):

        number = group.find("number")

        if number is not None and number.text == str(group_number):

            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = find_incoming_by_group_number(5)

if result:
    logging.info(f"Incoming value for group number 5 = {result}")
else:
    logging.info("Group not found")