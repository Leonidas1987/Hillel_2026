# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}x{multiplier}={result}")
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def calculate_sum(first_number, second_number):

    return first_number + second_number


print(calculate_sum(5, 7))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


print(calculate_average([2, 4, 6, 8]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    """Повертає рядок у зворотному порядку."""
    return text[::-1]


print(reverse_string("Python"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):

    if not words:
        return ""

    return max(words, key=len)


print(find_longest_word(["cat", "elephant", "dog"]))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # -1

# task 7
def has_more_than_ten_unique_characters(text):
    """Перевіряє, чи містить рядок більше 10 унікальних символів."""
    return len(set(text)) > 10


print(has_more_than_ten_unique_characters("abcdefghijk"))
# task 8
def contains_letter_h(word):
    """Перевіряє, чи містить слово літеру h незалежно від регістру."""
    return "h" in word.lower()


print(contains_letter_h("Hello"))
# task 9
def get_strings(values):
    """Повертає новий список, що містить лише рядки з переданого списку."""
    return [value for value in values if isinstance(value, str)]


print(get_strings([1, "apple", 3.5, "banana", True]))
# task 10
def calculate_even_sum(numbers):
    """Повертає суму всіх парних чисел у списку."""
    return sum(number for number in numbers if number % 2 == 0)


print(calculate_even_sum([1, 2, 3, 4, 5, 6]))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""