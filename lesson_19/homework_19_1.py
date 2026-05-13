import logging
from datetime import datetime

TARGET_KEY = "Key TSTFEED0300|7E3E|0400"
HB_FILE = "hblog.txt"
LOG_FILE = "hb_test.log"


def filter_lines(filepath, key):
    filtered = []
    with open(filepath, "r") as f:
        for line in f:
            if key in line:
                filtered.append(line.strip())
    return filtered


def get_timestamp(line):
    ts_index = line.find("Timestamp ")
    ts_str = line[ts_index + len("Timestamp "):ts_index + len("Timestamp ") + 8]
    return datetime.strptime(ts_str, "%H:%M:%S")


def analyze_heartbeat(filtered_lines):
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format="%(levelname)s - %(message)s",
        filemode="w",
        encoding="utf-8"
    )

    for i in range(len(filtered_lines) - 1):
        current_ts = get_timestamp(filtered_lines[i])
        next_ts = get_timestamp(filtered_lines[i + 1])

        diff = abs((current_ts - next_ts).total_seconds())

        if 31 < diff < 33:
            logging.warning(f"Timestamp {current_ts.strftime('%H:%M:%S')} — heartbeat {diff:.0f} сек (WARNING)")
        elif diff >= 33:
            logging.error(f"Timestamp {current_ts.strftime('%H:%M:%S')} — heartbeat {diff:.0f} сек (ERROR)")

    print(f"Аналіз завершено. Результат у файлі {LOG_FILE}")


if __name__ == "__main__":
    filtered = filter_lines(HB_FILE, TARGET_KEY)
    print(f"Знайдено рядків з ключем: {len(filtered)}")
    analyze_heartbeat(filtered)