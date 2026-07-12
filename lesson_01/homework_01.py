# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


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

apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(f"В саду посадили {apple_trees} яблуні, {pear_trees} груш і {plum_trees} слив.")
print(f"Всього в саду посадили {total_trees} дерев.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temperature_before = 5
temperature_after = temperature_before - 10
temperature_evening = temperature_after + 4
print(f"Надвечір температура повітря була {temperature_evening} градусів.")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys_total = 24
girls_total = boys_total // 2
boys_present = boys_total - 1
girls_present = girls_total - 2
children_today = boys_present + girls_present
print(f"сьогодні у театральному гуртку було {boys_present} хлопчики та {girls_present} дівчаток.")
print(f"Всього сьогодні на занятях {children_today} дітей.")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

book1_price = 8
book2_price = book1_price + 2
book3_price = (book1_price + book2_price) // 2
total_cost = book1_price + book2_price + book3_price
print(f"Перша книжка коштує {book1_price} грн, друга {book2_price} грн, а третя {book3_price} грн.")
print(f"За усі книги разом треба заплатити {total_cost} грн.")