if __name__ == "__main__":
    pass

n = int(input("n: "))
x = float(input("x (|x| < 1): "))

s = 0.0
for k in range(1, n + 1):
    s += ((-1) ** (k - 1)) * (x ** k) / k

print(s)
