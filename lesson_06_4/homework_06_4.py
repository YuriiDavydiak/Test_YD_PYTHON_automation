numbers = [1, 4, 7, 10, 3, 8, 6]

sum_even = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num

print(sum_even)