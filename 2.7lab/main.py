if __name__ == "__main__":
    pass
# Создаем строку с числами как в файле
text = """   123   
  45  
    6   
  789"""

count = 0
total = 0

lines = text.split('\n')

for line in lines:
    line = line.strip()
    if line:
        num = int(line)
        count += 1
        total += num

print(f"Количество чисел: {count}")
print(f"Сумма чисел: {total}")
