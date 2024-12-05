from itertools import product

# Генеруємо всі можливі комбінації трьох кубиків
variants = list(product(range(1, 7), repeat=3))
s11 = 0
s12 = 0
for variant in variants:
    if sum(variant) == 11:
        s11 += 1
    elif sum(variant) == 12:
        s12 += 1

print(f"Ймовірність випадіння суми 11: {s11 / len(variants)}")
print(f"Ймовірність випадіння суми 12: {s12 / len(variants)}")
