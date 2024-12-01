import sympy as sp

# Оголосимо змінну x
x = sp.symbols('x')

# Функції для диференціювання
f1 = x**3 / 3 + x**2 / 2 - 2 * x
f2 = sp.sqrt(x**2 + 1)
f3 = 1 / sp.sqrt(x**2 + 1)

# Похідні функцій
df1 = sp.diff(f1, x)
df2 = sp.diff(f2, x)
df3 = sp.diff(f3, x)

# Точки, у яких обчислюємо похідні
points = [1, -1/2]

# Обчислення значень похідних у точках
results = {
    "f1": {point: df1.subs(x, point) for point in points},
    "f2": {point: float(df2.subs(x, point)) for point in points},
    "f3": {point: float(df3.subs(x, point)) for point in points}
}

print(results)
