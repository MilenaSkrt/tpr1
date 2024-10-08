import numpy as np

def f(x):
    return x**2 - 2*x - 2*np.cos(x)

def find_minimum_using_broken_lines(start, end, num_points=100):
    iterations = 0  # Инициализируем счётчик итераций
    x_values = np.linspace(start, end, num_points)
    y_values = f(x_values)
    
    # Находим минимальное значение и соответствующее x
    min_index = np.argmin(y_values)
    
    # Увеличиваем счётчик итераций
    iterations += 1
    
    return x_values[min_index], y_values[min_index], iterations

# Задаем границы интервала
start = 0.5
end = 1.0

# Находим минимум
min_x, min_f, iterations = find_minimum_using_broken_lines(start, end)

print(f"Минимум функции f(x) достигается в x = {min_x:.4f}, f(x) = {min_f:.4f}")
print(f"Количество итераций: {iterations}")
