def reverse_iterator(lst):
    return iter(lst[::-1])

print("Зворотний список:")
for item in reverse_iterator([1, 2, 3, 4, 5, 6, 7, 8]):
    print(item, end=" ")
print()


def even_iterator(n):
    return iter(range(0, n + 1, 2))

print("Послідовність парних чисел до 30 через ітератор:")
for num in even_iterator(30):
    print(num, end=" ")
print()