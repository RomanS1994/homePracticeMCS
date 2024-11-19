import matplotlib.pyplot as plt
import numpy as np


# Функція для обчислення модуля вектора
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))


# Створення вектора
vector_a = np.array([2, 3])


# Обчислення модуля вектора
magnitude_a = compute_vector_magnitude(vector_a)


# Вивід результату
print(f"Вектор A: {vector_a}")
print(f"Модуль вектора A: {magnitude_a:.2f}")


# Візуалізація вектора на площині
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale=1, color='b', label='Вектор A')


# Додавання підпису з модулем вектора
plt.text(vector_a[0] / 2, vector_a[1] / 2, f'Modulus: {magnitude_a:.2f}', color='r')


# Налаштування вигляду графіка
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Модуль вектора на площині')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()
plt.show()
