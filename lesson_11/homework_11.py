def sum_num(raw):
    """Повертає суму чисел у рядку, розділених комою."""
    return sum(int(elem) for elem in raw.split(","))


arr = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for raw in arr:
    try:
        print(sum_num(raw))
    except ValueError:
        print("Не можу це зробити!")