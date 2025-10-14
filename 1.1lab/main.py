if __name__ == "__main__":
    pass
# ЕГЭ профиль — https://math-ege.sdamgia.ru/problem?id=77421
# Найти min y = x**3 - 27*x на [0; 4]
def f(x):
    return x**3 - 27*x
# кандидаты: концы отрезка и критическая точка из f'(x)=3x^2-27=0 → x=3
print(min(f(0), f(3), f(4)))  # выводим только число
