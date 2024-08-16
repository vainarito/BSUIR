import numpy as np
import matplotlib.pyplot as plt

# Ваша одномерная выборка данных
data = [
    7.79, 4.83, 2.67, 6.31, 7.55, 2.29, 6.04, 4.23, 7.37, 5.98, 5.61, 3.23, 5.59, 0.79, 4.08, 2.20, 5.56, 7.59, 2.65, 8.08, 6.36, 2.18, 1.33, 6.34, 5.51,
    8.23, 7.51, 3.44, 2.90, 6.17, 1.27, 5.30, 5.08, 3.43, 5.88, 3.54, 7.67, 3.37, 2.40, 5.27, 4.49, 0.86, 8.32, 6.59, 5.15, 5.01, 1.92, 2.60, 6.71, 7.35,
    0.90, 6.77, 3.99, 6.39, 3.70, 0.76, 3.24, 3.15, 6.69, 4.79, 5.75, 6.13, 7.66, 3.02, 5.93, 2.31, 6.82, 1.66, 4.73, 4.90, 3.43, 3.68, 3.19, 1.19, 2.99,
    6.46, 3.36, 6.51, 6.47, 8.34, 8.10, 5.52, 8.03, 4.38, 5.30, 6.18, 6.89, 7.04, 7.82, 6.49, 2.66, 7.28, 1.39, 4.07, 6.53, 6.95, 5.13, 5.02, 3.26, 3.77
]

# Заданные значения
k = 10  # Количество интервалов

# Расчет границ интервалов
hist, bin_edges = np.histogram(data, bins=k)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Построение гистограммы
plt.figure(figsize=(8, 6))
plt.hist(data, bins=k, edgecolor='black', alpha=0.7)

# Добавление подписей осей и заголовка
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма равновероятным способом')

# Отображение гистограммы
plt.show()