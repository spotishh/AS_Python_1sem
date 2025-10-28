if __name__ == "__main__":
    pass
nums = [7, 3, 10, 5, 8, 2, 9]

# находим индексы минимального и максимального элементов
i1 = nums.index(min(nums))
i2 = nums.index(max(nums))

# считаем сумму элементов между ними, включая оба
result = sum(nums[min(i1, i2) : max(i1, i2) + 1])

print(result)
