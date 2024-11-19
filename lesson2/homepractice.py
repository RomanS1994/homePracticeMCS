import numpy as np
a = np.array([[3, 0, 0], [1, 2, 0], [0, 1, -1]])
b = np.array([30, 18, 2])
x = np.linalg.solve(a, b)


print ("Матриця A:\n", a)
print ("Вектор b:\n", b)
print ("Розв'язання системи:\n", x)


res = 0.5*x[2]+x[0]*0.5*x[1]
print(res)
