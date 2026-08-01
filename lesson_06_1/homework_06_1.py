string_text = input("Введіть рядок: ")

unique_characters = set(string_text)
unique_characters_count = len(unique_characters)

print(unique_characters_count >= 10)