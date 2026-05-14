from datetime import datetime
from logger import get_logger

TARGET_KEY = "Key TSTFEED0300|7E3E|0400"
HB_FILE = "hblog.txt"

logger = get_logger()


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
    for i in range(len(filtered_lines) - 1):
        current_ts = get_timestamp(filtered_lines[i])
        next_ts = get_timestamp(filtered_lines[i + 1])

        diff = abs((current_ts - next_ts).total_seconds())

        if 31 < diff < 33:
            logger.warning(f"Timestamp {current_ts.strftime('%H:%M:%S')} — heartbeat {diff:.0f} сек (WARNING)")
        elif diff >= 33:
            logger.error(f"Timestamp {current_ts.strftime('%H:%M:%S')} — heartbeat {diff:.0f} сек (ERROR)")

    print(f"Аналіз завершено. Результат у файлі hb_test.log")


if __name__ == "__main__":
    filtered = filter_lines(HB_FILE, TARGET_KEY)
    print(f"Знайдено рядків з ключем: {len(filtered)}")
    analyze_heartbeat(filtered)