import csv


def remove_duplicates_from_two_files(file_1, file_2, result_file):
    unique_rows = []
    seen = set()

    for file in [file_1, file_2]:
        with open(file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                row_tuple = tuple(row)

                if row_tuple not in seen:
                    seen.add(row_tuple)
                    unique_rows.append(row)

    with open(result_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(unique_rows)

    print(f"Result saved to {result_file}")


if __name__ == "__main__":
    file_1 = "ideas_for_test/work_with_csv/random.csv"
    file_2 = "ideas_for_test/work_with_csv/random-michaels.csv"
    result_file = "result_davydyak.csv"

    remove_duplicates_from_two_files(file_1, file_2, result_file)