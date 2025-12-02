if __name__ == "__main__":
    pass
# Представим, что у нас есть содержимое файла
file_content = "12abcde" 

# Берем первые два символа
first_two = file_content[:2]

if len(first_two) >= 2 and first_two[0].isdigit() and first_two[1].isdigit():
    print("Да, первые два символа - цифры")
    number = int(first_two)
    if number % 2 == 0:
        print(f"Число {number} четное")
    else:
        print(f"Число {number} нечетное")
else:
    print("Нет, первые два символа не цифры")
