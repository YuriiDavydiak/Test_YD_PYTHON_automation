# task 1
"""
Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)


# task 2
"""  
Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    return a + b

result = sum_numbers(3, 5)
print(result)


# task 3
"""  
Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(numbers):
    return sum(numbers) / len(numbers)

nums = [9,12,25,48]
print(average(nums))

# task 4
"""  
Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

print(reverse_string("я несу гусеня"))

# task 5
"""  
Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def get_longest_word(words):

    sorted_words = sorted(words, key=len, reverse=True)
    return sorted_words[0]


print(get_longest_word(["пістолет", "кулемет", "автомат", "артилерія"]))


# task 6
"""  
Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
"""
Checks if the input string contains more than 10 unique symbols.
"""
def has_more_than_10_unique_symbols(text):
    unique_symbols = set(text)
    return len(unique_symbols) > 10

print(has_more_than_10_unique_symbols("hello world"))

# task 8
"""
Calculates the sum of all even numbers in a list.
"""
def sum_even_numbers(numbers):

    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))

# task 9

"""
Cleans the text:
- replaces line breaks with spaces
- replaces '....' with space
- removes extra spaces
"""

def clean_text(text):

    text = text.replace("\n", " ")
    text = text.replace("....", " ")

    # прибираємо зайві пробіли
    text = " ".join(text.split())

    return text


print(clean_text("Wat's....\nup   bro!"))

# task 10

"""
Check how many times a specific letter appears in the text.
"""

def count_letter(text, letter):

    return text.lower().count(letter.lower())


print(count_letter("Would you tell me, please, which way I ought to go from here?", "e"))

