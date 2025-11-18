if __name__ == "__main__":
    pass
def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Элемент [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print()

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: матрицы разного размера!")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Ошибка: нельзя умножить матрицы таких размеров!")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            summa = 0
            for k in range(len(matrix2)):
                summa += matrix1[i][k] * matrix2[k][j]
            row.append(summa)
        result.append(row)
    return result

def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

if __name__ == "__main__":
    print("=== ПРОВЕРКА МОДУЛЯ ===")
    
    print("\n1. Ввод матрицы A:")
    A = input_matrix()
    print("Матрица A:")
    print_matrix(A)
    
    print("\n2. Транспонирование матрицы A:")
    A_transposed = transpose_matrix(A)
    print("Транспонированная матрица A:")
    print_matrix(A_transposed)
    
    print("\n3. Ввод матрицы B для сложения:")
    B = input_matrix()
    print("Матрица B:")
    print_matrix(B)
    
    print("\n4. Сложение матриц A и B:")
    C = add_matrices(A, B)
    if C:
        print("Результат сложения:")
        print_matrix(C)
    
    print("\n5. Ввод матрицы D для умножения:")
    D = input_matrix()
    print("Матрица D:")
    print_matrix(D)
    
    print("\n6. Умножение матриц A и D:")
    E = multiply_matrices(A, D)
    if E:
        print("Результат умножения:")
        print_matrix(E)
