# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

# Given list of tuples:
# name, surname, age, profession, city

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]


# Task 01
# Додаємо власний запис на початок списку

my_record = (
    'Leon',
    'Fon',
    39,
    'QA Tester',
    'Rishon LeZion'
)

people_records.insert(0, my_record)

print("Task 01")
print("Список після додавання нового запису:")

for index, person in enumerate(people_records):
    print(index, person)


# Task 02
# Міняємо місцями елементи з індексами 1 та 5

people_records[1], people_records[5] = (
    people_records[5],
    people_records[1]
)

print("\nTask 02")
print("Список після обміну елементів з індексами 1 та 5:")

for index, person in enumerate(people_records):
    print(index, person)


# Task 03
# Перевіряємо вік людей з індексами 6, 10 та 13

indexes_to_check = (6, 10, 13)

all_people_are_30_or_older = all(
    people_records[index][2] >= 30
    for index in indexes_to_check
)

print("\nTask 03")
print("Люди, яких перевіряємо:")

for index in indexes_to_check:
    person = people_records[index]

    print(
        f"Індекс {index}: "
        f"{person[0]} {person[1]}, "
        f"вік — {person[2]}"
    )

print(
    "Чи всі люди з індексами 6, 10 та 13 "
    f"мають вік не менше 30 років: "
    f"{all_people_are_30_or_older}"
)
