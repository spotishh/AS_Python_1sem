try:
    with open('f.txt', 'r') as file:
        first_two = file.read(2)
        
        if len(first_two) >= 2 and first_two[0].isdigit() and first_two[1].isdigit():
            print(f"Первые два символа: '{first_two}'")
            print("Да, первые два символа - цифры")
            
            number = int(first_two)
            print(f"Образованное число: {number}")
            
            if number % 2 == 0:
                print(f"Число {number} - ЧЕТНОЕ")
            else:
                print(f"Число {number} - НЕЧЕТНОЕ")
        else:
            print(f"Первые два символа: '{first_two}'")
            print("Нет, первые два символа не являются обе цифрами")
            
except FileNotFoundError:
    print("Ошибка: Файл f.txt не найден!")
    print("Создайте файл f.txt с данными")
except Exception as e:
    print(f"Произошла ошибка: {e}")
