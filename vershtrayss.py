import numpy as np
from math import pi, cos, log

from matplotlib import pyplot as plt


def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
    else a * power(a, n - 1))


x_data = np.arange(-2, 2.01, 0.01)
n = 100
b = 0.9
eps = 1e-4
print('b^n = {:5.3e}'.format(power(b, n)))
m = round(log(eps) / log(b)) + 1
print('достаточное количество членов ряда : ', m)
n = m
a = 3
y_data = np.array([])
for x in x_data:
    y = 0
    for i in range(n):
        ai = power(a, i) * x * pi
        bi = power(b, i)
        y += cos(ai) * bi
    y_data = np.append(y_data, y)
print("end")

plt.figure(figsize=(12, 7))
plt.plot(x_data, y_data, alpha=0.7, label="first")

plt.show()
