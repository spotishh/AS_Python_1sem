if __name__ == "__main__":
    pass
# а) Словарь с числами от 1 до 15 и их квадратами
print("а) Словарь с квадратами чисел:")
squares_dict = {}
for i in range(1, 16):
    squares_dict[i] = i * i

print(squares_dict)
print()

# б) Словарь с количеством символов в строке
print("б) Словарь с количеством символов:")
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(f"Для строки '{text}':")
print(char_count)
print()

# в) Фильтрация словаря
print("в) Фильтрация словаря:")
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {}

for key, value in original_dict.items():
    if value > 2:
        filtered_dict[key] = value

print(f"Исходный словарь: {original_dict}")
print(f"После фильтрации: {filtered_dict}")
