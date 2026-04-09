def sum_numbers(s):

    try:
        numbers = s.split(",")
        total = 0

        for num in numbers:
            total += int(num)

        return total

    except ValueError:
        return "Не можу це зробити!"


data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    print(sum_numbers(item))