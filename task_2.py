import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# функція та параметри
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
y_max = f(b) # максимальне значення Y 

# реалізація методу Монте-Карло
N = 100000  # кількість випадкових пострілів

# генеруємо випадкові точки
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, y_max, N)

# умова: y_point < f(x_point)
points_under_curve = np.sum(y_rand < f(x_rand))

# площа описуючого прямокутника S_rect = (b-a) * f(b)
area_rectangle = (b - a) * y_max

# інтеграл ≈ (k / N) * S_rect
integral_mc = (points_under_curve / N) * area_rectangle

# перевірка quad та аналітично
integral_quad, error = spi.quad(f, a, b)
integral_analytical = (2**3)/3 - (0**3)/3

print(f"Результат Монте-Карло: {integral_mc}")
print(f"Результат SciPy quad:  {integral_quad}")
print(f"Аналітичний результат: {integral_analytical}")
