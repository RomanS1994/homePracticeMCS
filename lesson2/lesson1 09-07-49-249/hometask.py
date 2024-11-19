import numpy as np

# Матриця A та вектор b
A = np.array([[-1, 1, 2],
              [0, -1, -3],
              [4, -3, 2]])

B = np.array([[1],
 [-4], 
 [7]])


# Напиши функцію для вирішення системи методом Крамера
def solve_cramer(a, b, verbose=False):
    delta = np.linalg.det(a) 
    b = b.T
    if delta == 0:
        return ('Матриця вироджена A')
    
    A1 = a.copy()
    A2 = a.copy()
    A3 = a.copy()
    
    A1[:, 0] = b
    A2[:, 1] = b  
    A3[:, 2] = b  
    

    delta_1 = np.linalg.det(A1)
    delta_2 = np.linalg.det(A2)
    delta_3 = np.linalg.det(A3)
    

    x1 = delta_1 / delta
    x2 = delta_2 / delta
    x3 = delta_3 / delta
    
    return x1, x2, x3

print(f"Вектор рішення: \r\n {solve_cramer(A, B)}")
