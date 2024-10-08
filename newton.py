import numpy as np
import matplotlib.pyplot as plt

# Определим функцию f(x)
def f(x):
    return x ** 2 - 2 * x - 2 * np.cos(x)

# Определим первую производную f'(x)
def f_prime(x):
    return 2 * x - 2 + 2 * np.sin(x)

# Определим вторую производную f''(x)
def f_double_prime(x):
    return 2 + 2 * np.cos(x)

# Метод Ньютона для нахождения минимума
def newtons_method(x0, tol=1e-6, max_iter=100):
    x = x0
    iteration_count = 0  # Счётчик итераций
    for i in range(max_iter):
        f_prime_value = f_prime(x)
        f_double_prime_value = f_double_prime(x)

        if f_double_prime_value == 0:  # Проверка на случай деления на ноль
            print("Вторичная производная равна нулю, метод не может продолжать.")
            break

        # Обновление x согласно методу Ньютона
        x_new = x - f_prime_value / f_double_prime_value

        # Проверяем, находимся ли мы в пределах заданного диапазона
        if x_new < 0.5 or x_new > 1:
            print(f"Выход за пределы: {x_new}. Прекращение.")
            break

        # Проверяем, достигнута ли точность
        if abs(x_new - x) < tol:
            iteration_count += 1  # Увеличиваем счётчик итераций
            print(f"Достигнута точность на итерации {i + 1}. x = {x_new:.5f}")
            print(f"Общее количество итераций: {iteration_count}")
            return x_new

        x = x_new
        iteration_count += 1  # Увеличиваем счётчик итераций

    print(f"Достигнуто максимальное количество итераций: {max_iter}.")
    return x

# Начальное значение
x0 = 0.75  # Выбираем начальное значение между 0.5 и 1

# Запуск метода Ньютона
minimum = newtons_method(x0)
print(f"Минимум функции достигается в x = {minimum:.5f}, f(x) = {f(minimum):.5f}")

# Построение графика
x_values = np.linspace(0.5, 1.5, 400)
f_values = f(x_values)
f_prime_values = f_prime(x_values)
f_double_prime_values = f_double_prime(x_values)

plt.figure(figsize=(12, 8))

# График функции
plt.subplot(3, 1, 1)
plt.plot(x_values, f_values, label='f(x)', color='blue')
plt.scatter([minimum], [f(minimum)], color='red', label='Минимум')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()

# График первой производной
plt.subplot(3, 1, 2)
plt.plot(x_values, f_prime_values, label="f'(x)", color='green')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.title('График первой производной f\'(x)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.legend()

# График второй производной
plt.subplot(3, 1, 3)
plt.plot(x_values, f_double_prime_values, label="f''(x)", color='orange')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.title('График второй производной f\'\'(x)')
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.legend()

plt.tight_layout()
plt.show()
