import numpy as np 
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

task1 = b.dot(a)
# print(task1)


c = np.array([[2, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
task2 = c.dot(d)
# print(task2)

f = np.array([[9, 2], [7, 3]])
e = np.array([[5, 4], [2, 1]])
task3 = f.dot(e)
# print(task3)



r = np.array([ [2, -9, -5], [-10, -1, -3], [-9, -6, 9]])
t = np.array([ [-10, -7, 1, 3], [-10, -7, 10, -9], [9, 4, -9, 7] ])
task4 = r.dot(t)
print(task4)



