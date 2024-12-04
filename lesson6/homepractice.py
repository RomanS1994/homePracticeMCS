def f(x):
    term1 = 4 / (1.2 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - 11) / 1.2)**2)
    term2 = 7 / (2.4 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - 15) / 2.4)**2)
    return 2 * (term1 + term2)

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, pi, sqrt, integrate
from scipy.integrate import quad


# Налаштування графіка
fig, ax = plt.subplots(figsize=(10, 10))
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.grid(True, linestyle='-.')

# Функція для NumPy
def f(x):
    return 2 * ((4 / (1.2 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - 11) / 1.2)**2)) +
            (7 / (2.4 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - 15) / 2.4)**2)))

# Побудова графіка
x = np.linspace(0, 24, 500)
y = f(x)

ax.plot(x, y, label="f(x)")
ax.set_title("Графік функції f(x)")
ax.legend()
plt.show()

# Символьна функція для SymPy
x_sym = symbols('x')
f_sym = 2 * ((4 / (1.2 * sqrt(2 * pi)) * exp(-0.5 * ((x_sym - 11) / 1.2)**2)) + \
        (7 / (2.4 * sqrt(2 * pi)) * exp(-0.5 * ((x_sym - 15) / 2.4)**2)))

# Невизначений інтеграл
indef_integral = integrate(f_sym, x_sym)

# Визначений інтеграл
a = 9
b = 18
def_integral = integrate(f_sym, (x_sym, a, b))

print("невизначений інтеграл:", indef_integral)
print(f"визначений інтеграл від {a} до {b}:", def_integral)
