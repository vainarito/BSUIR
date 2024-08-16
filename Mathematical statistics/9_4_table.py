import numpy as np

# Ваша одномерная выборка данных
data = [-7.56, -7.49, -7.49, -7.49, -7.36, -7.34, -7.32, -7.12, -7.11, -6.99, -6.95, -6.89, -6.82, -6.78, -6.78, -6.70,
        -6.64, -6.57, -6.51, -6.41, -6.39, -6.30, -6.23, -6.15, -6.15, -6.15, -6.14, -6.04, -6.03, -6.02, -5.83, -5.69,
        -5.64, -5.60, -5.40, -5.37, -5.36, -5.28, -5.05, -4.97, -4.93, -4.85, -4.78, -4.75, -4.37, -4.34, -4.18, -3.98,
        -3.94, -3.94, -3.87, -3.85, -3.78, -3.77, -3.66, -3.64, -3.51, -3.35, -3.31, -3.12, -3.10, -3.03, -2.98, -2.95,
        -2.92, -2.92, -2.87, -2.79, -2.79, -2.77, -2.74, -2.60, -2.59, -2.56, -2.49, -2.48, -2.48, -2.45, -2.44, -2.29,
        -2.26, -2.20, -2.04, -2.01, -1.92, -1.87, -1.85, -1.85, -1.83, -1.57, -1.57, -1.56, -1.51, -1.44, -1.32, -1.29,
        -1.17, -1.05, -0.94, -0.81, -0.77]

# Заданные значения
N = len(data)  # Общее количество чисел в выборке
k = 10  # Количество интервалов

# Расчет границ интервалов
n_values = N // k  # Число значений в каждом интервале
sorted_data = sorted(data)
intervals = [sorted_data[i*n_values:(i+1)*n_values] for i in range(k)]
min_values = [interval[0] for interval in intervals]
max_values = [interval[-1] for interval in intervals]

# Инициализация таблицы
table = []

# Расчет значений для каждого интервала
for j in range(k):
    Aj = min_values[j]
    Bj = max_values[j]
    hj = Bj - Aj
    vj = len(intervals[j])
    pj = vj / N
    fj = 1 / hj

    # Добавление значений в таблицу
    table.append([j + 1, Aj, Bj, hj, vj, pj, fj])

# Вывод таблицы
header = ['j', 'Aj', 'Bj', 'hj', 'vj', 'pj', 'fj']
print('{:^4s} | {:^9s} | {:^9s} | {:^6s} | {:^3s} | {:^9s} | {:^9s}'.format(*header))
print('-' * 63)
for row in table:
    print('{:^4.0f} | {:9.4f} | {:9.4f} | {:6.4f} | {:^3.0f} | {:9.4f} | {:9.4f}'.format(*row))