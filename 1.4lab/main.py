if __name__ == "__main__":
    pass
nums = [7, 3, 10, 5, 8, 2, 9]

i1 = nums.index(min(nums))
i2 = nums.index(max(nums))

result = sum(nums[min(i1, i2) : max(i1, i2) + 1])

print(result)
