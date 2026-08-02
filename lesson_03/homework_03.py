# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quote_count = alice_in_wonderland.count("'")
single_quotes = "'" * single_quote_count

print("\nTask 02")
print(f"Знайдені символи одинарної лапки: {single_quotes}")
print(f"Кількість символів: {single_quote_count}")
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\nTask 03")
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800

total_sea_area = black_sea_area + azov_sea_area

print("\nTask 04")
print(
    f"Площа Чорного моря — {black_sea_area} км², "
    f"а площа Азовського моря — {azov_sea_area} км²."
)
print(
    f"Разом Чорне та Азовське моря займають "
    f"{total_sea_area} км²."
)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375_291
first_and_second = 250_449
second_and_third = 222_950

third_warehouse = total_products - first_and_second
first_warehouse = total_products - second_and_third
second_warehouse = first_and_second - first_warehouse

print("\nTask 05")
print(f"На першому складі знаходиться {first_warehouse} товарів.")
print(f"На другому складі знаходиться {second_warehouse} товарів.")
print(f"На третьому складі знаходиться {third_warehouse} товарів.")

print(
    f"Перевірка: {first_warehouse} + {second_warehouse} + "
    f"{third_warehouse} = {first_warehouse + second_warehouse + third_warehouse}"
)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_months = 12 + 6
monthly_payment = 1_179

computer_price = payment_months * monthly_payment

print("\nTask 06")
print(f"Півтора року — це {payment_months} місяців.")
print(
    f"Вартість комп'ютера: "
    f"{payment_months} × {monthly_payment} = {computer_price} грн."
)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_a = 8_019 % 8
remainder_b = 9_907 % 9
remainder_c = 2_789 % 5
remainder_d = 7_248 % 6
remainder_e = 7_128 % 5
remainder_f = 19_224 % 9

print("\nTask 07")
print(f"a) Остача від ділення 8019 на 8: {remainder_a}")
print(f"b) Остача від ділення 9907 на 9: {remainder_b}")
print(f"c) Остача від ділення 2789 на 5: {remainder_c}")
print(f"d) Остача від ділення 7248 на 6: {remainder_d}")
print(f"e) Остача від ділення 7128 на 5: {remainder_e}")
print(f"f) Остача від ділення 19224 на 9: {remainder_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza_cost = 4 * 274
medium_pizza_cost = 2 * 218
juice_cost = 4 * 35
cake_cost = 1 * 350
water_cost = 3 * 21

total_order_cost = (
    large_pizza_cost
    + medium_pizza_cost
    + juice_cost
    + cake_cost
    + water_cost
)

print("\nTask 08")
print(f"Великі піци: 4 × 274 = {large_pizza_cost} грн.")
print(f"Середні піци: 2 × 218 = {medium_pizza_cost} грн.")
print(f"Сік: 4 × 35 = {juice_cost} грн.")
print(f"Торт: 1 × 350 = {cake_cost} грн.")
print(f"Вода: 3 × 21 = {water_cost} грн.")
print(f"Усього для замовлення потрібно {total_order_cost} грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8

pages_needed = (
    total_photos + photos_per_page - 1
) // photos_per_page

print("\nTask 09")
print(
    f"Ігор має {total_photos} фотографії, "
    f"а на одній сторінці можна розмістити "
    f"{photos_per_page} фотографій."
)
print(f"Ігорю знадобиться {pages_needed} сторінок.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1_600
fuel_per_100_km = 9
tank_capacity = 48

fuel_needed = distance_km // 100 * fuel_per_100_km

full_tanks_needed = (
    fuel_needed + tank_capacity - 1
) // tank_capacity

refueling_stops_on_route = full_tanks_needed - 1

print("\nTask 10")
print(
    f"Для подорожі на {distance_km} км потрібно "
    f"{fuel_needed} літри бензину."
)
print(
    f"{fuel_needed} ÷ {tank_capacity} = "
    f"{full_tanks_needed} повних баки."
)
print(
    f"Якщо перед виїздом бак уже повний, "
    f"під час дороги потрібно заїхати на заправку "
    f"{refueling_stops_on_route} рази."
)