if __name__ == "__main__":
    pass
def MinRec(A, n):
    if n == 1:
        return A[0]
    
    min_rest = MinRec(A, n - 1)
    
    if A[n - 1] < min_rest:
        return A[n - 1]
    else:
        return min_rest

arr1 = [3, 7, 2, 8, 1]
arr2 = [10, 5, 15, 3, 9]
arr3 = [-2, 0, -5, 4, -1]

min1 = MinRec(arr1, len(arr1))
min2 = MinRec(arr2, len(arr2))
min3 = MinRec(arr3, len(arr3))

print("Минимальный элемент массива 1:", min1)
print("Минимальный элемент массива 2:", min2)
print("Минимальный элемент массива 3:", min3)
