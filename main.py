import math
def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)  # функция: f(x) = x^2 - 2x - 2cos(x)
def dichotomy(a, b, eps):
    iterations = 0  # Инициализация счётчика итераций
    while (b - a) > eps:
        mid1 = a + (b - a) / 4  # первая середина интервала
        mid2 = b - (b - a) / 4  # вторая середина интервала

        if f(mid1) < f(mid2):
            b = mid2  # Убираем правую половину
        else:
            a = mid1  # Убираем левую половину

        iterations += 1  # Увеличиваем счётчик итераций

    return (a + b) / 2, iterations  # Возвращаем среднее значение и количество итераций

# Установим пределы и точность
a = 0.5
b = 1.0
eps = 1e-6

minimum_x, iterations = dichotomy(a, b, eps)
minimum_y = f(minimum_x)

print(f"Минимум функции достигнут при x = {minimum_x:.6f} и f(x) = {minimum_y:.6f}")
print(f"Количество итераций: {iterations}")



