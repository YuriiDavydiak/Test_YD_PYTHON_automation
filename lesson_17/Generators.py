
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("Парні числа до 20:")
    for num in even_numbers(20):
        print(num, end=" ")
    print()

    print("Фібоначчі до 100:")
    for num in fibonacci(100):
        print(num, end=" ")
    print()