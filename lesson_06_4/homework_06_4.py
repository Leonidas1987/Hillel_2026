numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

even_numbers_sum = sum(even_numbers)

print(f"Парні числа: {even_numbers}")
print(f"Сума всіх парних чисел: {even_numbers_sum}")