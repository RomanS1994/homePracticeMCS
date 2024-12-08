import numpy as np
import matplotlib.pyplot as plt
t = 3


    # випадкові кроки (-1 або +2)
def stock_price_at_time(t: int) -> int:
    steps = np.random.choice([-1, 2], size=t, p=[0.5, 0.5])
    return steps.sum()

#  процеси
def simulate_n_times(n: int, t: int) -> list:
    np.random.seed(42)  # Фіксуємо seed для відтворюваності
    results = [stock_price_at_time(t) for _ in range(n)]
    return results





    # гістограма
for n in [10, 100, 1000, 10000]:
    results = simulate_n_times(n, t)
    plt.hist(results, bins=20, alpha=0.6, edgecolor='black')
    plt.title(f'Гістограма для n={n} симуляцій, t={t}')
    plt.xlabel('Ціна')
    plt.ylabel('Частота')
    plt.show()


    print(f'Середнє значення для {n} симуляцій: {mean_price}')



