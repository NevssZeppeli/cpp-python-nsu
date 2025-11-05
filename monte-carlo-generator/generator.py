import numpy as np
from numpy.random import Generator, PCG64

def generate(pdf, limits, majorant, chunk_size, num_chunks):
    """
    Ключевая идея метода Монте-Карло: использовать случайность для получения приближённых, но статистически обоснованных решений. Допустим, метод иглы Бюффона.
    В принципе, метод Монте-Карло используется для решения детерменированных задач при помощи случайной выборки.

    Метод Неймана:
    1. Берем область Omega x [0, M], где M - мажоранта, то есть верхняя граница плотности
    2. Генерируем случайную выборку в этой области 
    3. Если y <= p(x), то такую точку учитываем, иначе - отбрасываем.

    pdf (p(x))- плотность вероятности
    limits (Omega) - определение прямоугольной области Omega через кортежи
    majorant (M) - максимальное значение для величины x_i
    chunk_size - количество кандидатов, генерируемых за один чанк
    num_chunks - количество чанков генерации

    accepted - массив "отобранных точек"
    n - размерность пространства
    rng - генератор чисел
    coordinates - массив координат

    Возвращаем list np.ndarray
    """
    accepted = [] 
    n = len(limits) 
    rng = Generator(PCG64())

    for j in range(num_chunks):
        coordinates = []

        # генерируем равномерно кандидатов x_i (в количестве chunk_size)
        for (x_min, x_max) in limits:
            coordinates.append(rng.uniform(x_min, x_max, size=chunk_size)) 
        
        # вычисляем плотность в данных точках (coordinates)
        p_values = pdf(*coordinates)

        # здесь мы генерируем точки в Omega x [0, M] - случайные высоты для проверки нахождения под кривой плотности
        x_i = rng.uniform(0.0, majorant, size=chunk_size)

        # булевый массив-маска, по которому мы отфильтруем точки в списке координат
        mask = x_i <= p_values

        # и далее мы отбираем нужные нам точки в numpy-массив размером (k, n), где k - количество принятых в чанке чисел 
        accepted_chunks = np.column_stack([coord[mask] for coord in coordinates])
        accepted.append(accepted_chunks)

    if accepted:
        result = np.vstack(accepted)
    else:
        result = np.empty((0, n))

    return result

   
"""
Доп - волновая функция. Подать её как p(x); визуализировать точки, которые нам подходят. По сути, это проекция на плоскость. Отрисовать боровский радиус. Отрисовать в matplotlib
"""


# волновая функция для основного состояния водорода имеет вид psi(r) = A*e^-r/a_0.

import matplotlib.pyplot as plt

# плотность вероятности |psi(r)|^2
def pdf_3d(x, y, z, a0 = 1.0):
    r = np.sqrt(x**2 + y**2 + z**2)
    
    return np.exp(-2 * r / a0)

a0 = 1.0

sample_3d = generate(
    pdf=lambda x, y, z: pdf_3d(x, y, z, a0=a0),
    limits=[[-5 * a0, 5 * a0], [-5 * a0, 5 * a0], [-5 * a0, 5 * a0]],
    majorant=1.0,
    chunk_size=20000,
    num_chunks=100 
)

x = sample_3d[:, 0]
y = sample_3d[:, 1]

N_bins = 50
range_xy = [[-5,5], [-5,5]]
counts, x_edges, y_edges = np.histogram2d(x, y, bins=N_bins, range=range_xy)


fig, ax = plt.subplots(figsize=(7, 7))
im = ax.hist2d(x, y, bins=50, range=[[-5,5], [-5,5]], cmap='bwr')

theta = np.linspace(0, 2*np.pi, 300)
circle_x = a0 * np.cos(theta)
circle_y = a0 * np.sin(theta)
ax.plot(circle_x, circle_y, 'r--', linewidth=2, label=r'Боровский радиус $a_0$')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')
ax.grid(True, alpha=0.6)
ax.legend()
plt.colorbar(im[3])

plt.tight_layout()
plt.show()



