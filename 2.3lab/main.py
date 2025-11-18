if __name__ == "__main__":
    pass
def diagonal_sum(matrix, choice):
    n = len(matrix)
    summa = 0

    if choice == 1:
        for i in range(n):
            for j in range(n):
                if i == j:
                    summa += matrix[i][j]
    else:
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    summa += matrix[i][j]

    return summa


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матрица:")
for row in matrix:
    print(row)

choice = int(input("1 - главная, 2 - побочная: "))
result = diagonal_sum(matrix, choice)
print("Сумма =", result)
