import numpy as np
import matplotlib.pyplot as plt

# Параметри гамма-розподілу
shape = 0.3  # Параметр форми (k)
scale = 1.1  # Параметр шкали (θ)

# Симуляція зміни ціни акцій для заданого часу t
def stock_price_at_time(t: int) -> float:
    steps = np.random.gamma(0.3, 1.1, size=t)  # Генеруємо t значень
    return steps.sum()

# Симуляція n разів для заданого часу t
def simulate_n_times(n: int, t: int) -> list:
    np.random.seed(42)  # Фіксуємо seed для відтворюваності
    results = [stock_price_at_time(t) for _ in range(n)]
    return results

# Симуляція для різних значень часу t
t_values = range(1, 61, 2)  # Від 1 до 60 з кроком 2
n = 100  # Кількість симуляцій для кожного t

# Аналіз і побудова гістограм
for t in t_values:
    results = simulate_n_times(n, t)
    
    # Будуємо гістограму
    plt.hist(results, bins=20, alpha=0.6, edgecolor='black')
    plt.title(f'Гістограма для n={n} симуляцій, t={t}')
    plt.xlabel('Ціна')
    plt.ylabel('Частота')
    plt.show()
    
    # Середнє значення
    mean_price = np.mean(results)
    print(f'Середнє значення для t={t}: {mean_price}')
