import numpy as np
import matplotlib.pyplot as plt  # Импортируем библиотеку для построения графиков

def f(x):
    return x ** 2 - 2 * x - 2 * np.cos(x)

def find_minimum_using_broken_lines(start, end, num_points=100):
    iterations = 0  # Инициализируем счётчик итераций
    x_values = np.linspace(start, end, num_points)
    y_values = f(x_values)

    # Находим минимальное значение и соответствующее x
    min_index = np.argmin(y_values)

    # Увеличиваем счётчик итераций
    iterations += 1

    return x_values[min_index], y_values[min_index], iterations, x_values, y_values

# Задаем границы интервала
start = 0.5
end = 1.0

# Находим минимум
min_x, min_f, iterations, x_values, y_values = find_minimum_using_broken_lines(start, end)

print(f"Минимум функции f(x) достигается в x = {min_x:.4f}, f(x) = {min_f:.4f}")
print(f"Количество итераций: {iterations}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.plot(min_x, min_f, 'ro', label='Минимум')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
