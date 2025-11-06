if __name__ == "__main__":
    pass
nums = [3, 10, 25, 7, 40, 13, 5]

res = [x for x in nums if x % 5 == 0]

res.sort(reverse=True)

print(res)


