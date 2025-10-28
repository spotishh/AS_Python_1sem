if __name__ == "__main__":
    pass
nums = [3, 10, 25, 7, 40, 13, 5]

# выбираем числа, которые делятся на 5 без остатка
res = [x for x in nums if x % 5 == 0]

# сортируем по убыванию
res.sort(reverse=True)

print(res)


