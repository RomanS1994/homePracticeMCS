import time
from scipy.optimize import linprog

start = time.time()

# Цільова функція — на мінімум
c = [-2, -9, -6]

# Коефіцієнти при нерівностях
A_ub = [
    [12, 6, 2],
    [12, 24, 18],
    [12, 18, 12],
]
b_ub = [360, 192, 180]  # Результати при нерівностях

# Оптимізація
result = linprog(c, A_ub, b_ub)




print("Оптимальний розподіл робіт:", result.x)

    # Підрахунок максимального доходу
x1, x2, x3 = result.x
print(x1, x2, x3)
total_income = (12*x1 + 6*x2 + 2*x3) * 2 + (12*x1 + 24*x2 + 18*x3) * 9 + (12*x1 + 18*x2 + 12*x3) * 6
print("Максимальний місячний дохід:", total_income)



stop = time.time()
print("Час виконання:", stop - start)
