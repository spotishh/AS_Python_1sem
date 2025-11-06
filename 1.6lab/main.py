if __name__ == "__main__":
    pass

s = input("Введите строку: ")

if len(s) > 1:
    new_s = s[-1] + s[1:-1] + s[0]
else:
    new_s = s

print("Новая строка:", new_s)
