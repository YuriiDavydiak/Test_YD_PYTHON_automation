def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції {func.__name__}: {type(e).__name__}: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)