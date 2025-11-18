if __name__ == "__main__":
    pass
def InvertDigits(K):
    s = str(K)
    perevernutaya = s[::-1]
    result = int(perevernutaya)
    return result

print(InvertDigits(123))
print(InvertDigits(100))
print(InvertDigits(7))
print(InvertDigits(98765))
