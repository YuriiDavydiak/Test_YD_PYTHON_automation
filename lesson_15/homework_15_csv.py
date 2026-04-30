import csv

file_1 = "ideas_for_test/work_with_csv/random.csv"
file_2 = "ideas_for_test/work_with_csv/random-michaels.csv"

result_file = "result_davydіak.csv"

unique_rows = set()

with open(file_1, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        unique_rows.add(tuple(row))

with open(file_2, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        unique_rows.add(tuple(row))

with open(result_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for row in unique_rows:
        writer.writerow(row)

print("Файл result_davydіak.csv створено успішно")