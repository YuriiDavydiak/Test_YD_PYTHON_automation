# task 01 == Виправте синтаксичні помилки # виправив
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки # виправив
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print # вставив
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була # зробив
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних # виправив
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 # порахував
# та виведіть його для користувача
perimetery = ? + ? + ? + ?
print()

storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apples = 4
pears = apples + 5
plums = apples - 2

total_trees = apples + pears + plums

print(f"У саду посадили {apples} яблуні.")
print(f"Груш посадили {pears}.")
print(f"Слив посадили {plums}.")
print(f"Всього в саду посадили {total_trees} дерев.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature = 5
temperature = temperature - 10
temperature = temperature + 4

print(temperature)

або

temperature = 5
print(f"До обіду було {temperature}°C.")

temperature = temperature - 10
print(f"Після обіду стало {temperature}°C.")

temperature = temperature + 4
print(f"Надвечір стало {temperature}°C.")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = boys // 2

# Сьогодні
boys_today = boys - 1
girls_today = girls - 2

total_today = boys_today + girls_today

print(f"Сьогодні у гуртку {total_today} дітей.")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1 = 8
book2 = book1 + 2
book3 = (book1 + book2) / 2

total = book1 + book2 + book3

print(f"Перша книга коштує {book1} грн.")
print(f"Друга книга коштує {book2} грн.")
print(f"Третя книга коштує {book3} грн.")
print(f"Усі книги разом коштують {total} грн.")
