
# task 01

alice_in_wonderland = """ 
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""

# task 02

print("Кількість одинарних лапок:", alice_in_wonderland.count("'"))

# task 03

print(alice_in_wonderland)

# task 04

black_sea = 436_402
azov_sea = 37_800

total_area = black_sea + azov_sea

print(f"Площа Чорного моря становить {black_sea} км².")
print(f"Площа Азовського моря становить {azov_sea} км².")
print(f"Разом вони займають {total_area} км².")

# task 05

total = 375_291
first_second = 250_449
second_third = 222_950

third = total - first_second
first = total - second_third
second = first_second - first

print(f"На першому складі {first} товарів.")
print(f"На другому складі {second} товарів.")
print(f"На третьому складі {third} товарів.")

# task 06

monthly_payment = 1179
months = 12 * 1.5

total_price = monthly_payment * months

print(f"Платити потрібно {months} місяців.")
print(f"Щомісячний платіж становить {monthly_payment} грн.")
print(f"Вартість комп’ютера становить {total_price} грн.")

# task 07

print("a)", 8019 % 8)
print("b)", 9907 % 9)
print("c)", 2789 % 5)
print("d)", 7248 % 6)
print("e)", 7128 % 5)
print("f)", 19224 % 9)

# task 08

big_pizza = 4 * 274
medium_pizza = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

total = big_pizza + medium_pizza + juice + cake + water

print(f"Піца велика коштує {big_pizza} грн.")
print(f"Піца середня коштує {medium_pizza} грн.")
print(f"Сік коштує {juice} грн.")
print(f"Торт коштує {cake} грн.")
print(f"Вода коштує {water} грн.")
print(f"Загальна сума замовлення: {total} грн.")

# task 09

photos = 232
photos_per_page = 8

pages = photos // photos_per_page

print(f"Ігорю потрібно {pages} сторінок, щоб вклеїти всі фотографії.")

# task 10

distance = 1600
fuel_per_100km = 9
tank_capacity = 48

total_fuel = (distance / 100) * fuel_per_100km
tanks_needed = total_fuel / tank_capacity

print(f"Для подорожі потрібно {total_fuel} літрів бензину.")
print(f"Потрібно {int(tanks_needed)} повних баків бензину.")

print("Якщо родина виїжджає з повним баком, потрібно 2 заправки.")
print("Якщо бак спочатку порожній — потрібно 3 заправки.")
