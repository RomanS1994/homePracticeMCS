import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Налаштування графіка
fig, ax = plt.subplots()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.grid(True, linestyle='-.')

# Опис функції
x = sp.Symbol('x')
f = -3 * x**2 + 30 * x  # Нова функція
df = f.diff()  # Похідна

# Генерація числових даних
x1 = np.linspace(0, 15, 500)
f_lambd = sp.lambdify(x, f, 'numpy')
y = f_lambd(x1)

df_lambd = sp.lambdify(x, df, 'numpy')
dy = df_lambd(x1)

# Побудова графіків
ax.plot(x1, y, label=r"$f(x) = -3x^2 + 30x$", color='orange')  # Функція
ax.plot(x1, dy, label=r"$f'(x)$", color='blue')  # Похідна
ax.scatter(5, 75, color='red', label="Точки максимуму", zorder=100)  # Точкa максимуму




plt.show()
