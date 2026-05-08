def reverse_iterator(lst):
    return iter(lst[::-1])

def even_iterator(n):
    return iter(range(0, n + 1, 2))

if __name__ == "__main__":
    print("Зворотний список:")
    for item in reverse_iterator([1, 2, 3, 4, 5, 6, 7, 8]):
        print(item, end=" ")
    print()

    print("Парні числа до 30 через ітератор:")
    for num in even_iterator(30):
        print(num, end=" ")
    print()