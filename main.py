import matplotlib.pyplot as plt
import numpy as np
import math

# ВВОД НАЧАЛЬНЫХ УСЛОВИЙ И ВЫЧИСЛЕНИЕ МЕЛКОСТИ РАЗБИЕНИЯ
def start():
    while True:
        N = int(input('Введите ко-во точек разбиения: '))
        if N == 0:
            exit(1)
        ksi = str(input('Введите ориентацию оснащения: '))

        dx = 1 / N
        x = [0] * N
        y = [0] * N

        ksi_orientation(x, y, dx, ksi, N)
        plot_EXP()

# ПОСТРОЕНИЕ ПРЯМОУГОЛЬНИКОВ
def plot_Rectangle(x0, y0, h, dx):
    plt.vlines(x0, y0, h, colors='dimgray', linestyles='--')
    plt.vlines((x0 + dx), y0, math.e**(x0 + dx), colors='dimgray', linestyles='--')
    plt.hlines(y0, x0, (x0 + dx), colors='dimgray', linestyles='--')
    plt.hlines(h, x0, (x0 + dx), colors='dimgray', linestyles='--')

# ПОСТРОЕНИЕ ГРАФИКА ФУНКЦИИ e^x
def plot_EXP():
    x1 = np.linspace(0, 1, 1000)
    y1 = math.e**x1
    plt.plot(x1, y1, color = 'crimson', label=r"""$f(x) = e^x$""")
    plt.xlabel('Coordinate X')
    plt.ylabel('Coordinate Y')
    plt.title('Вычисление интегральной суммы для $f(x) = e^x$')
    plt.grid(True)
    plt.legend(loc = 'upper left')
    plt.show()

# ВЫЧИСЛЕНИЕ СУММЫ В ЗАВИСИМОСТИ ОТ ОРИЕНТАЦИИ ТОЧЕК РАЗБИЕНИЯ
def ksi_orientation(x, y, dx, ksi, N):
    theoretical_error = 0
    s = 0

    if ksi == 'L':
        x[0] = 0
        y[0] = 1
        s = dx * y[0]
        for i in range(1, N):
            x[i] = x[i-1] + dx
            y[i] = math.e ** x[i]
            s += dx * y[i]
        for i in range(0, N):
            plot_Rectangle(x[i], 0, y[i], dx)
        theoretical_error = math.e / (2 * N)

    elif ksi == 'R':
        x[0] = dx
        y[0] = math.e ** dx
        s = dx * y[0]
        for i in range(1, N):
            x[i] = x[i-1] + dx
            y[i] = math.e ** x[i]
            s += dx * y[i]
        for i in range(0, N):
            plot_Rectangle((x[i] - dx), 0, y[i], dx)
        theoretical_error = math.e / (2 * N)

    elif ksi == 'M':
        x[0] = dx/2
        y[0] = math.e ** (dx/2)
        s = dx * y[0]
        for i in range(1, N):
            x[i] = x[i-1] + dx
            y[i] = math.e ** x[i]
            s += dx * y[i]
        for i in range(0, N):
            plot_Rectangle((x[i] - 0.5*dx), 0, y[i], dx)
        theoretical_error = math.e / (24 * (N**2))

    error = abs(s - (math.e - 1))

    print('ЗНАЧЕНИЕ ИНТЕГРАЛЬНОЙ СУММЫ =', s)
    print('ТЕОРЕТИЧЕСКАЯ ПОГРЕШНОСТЬ =', theoretical_error)
    print('ПОГРЕШНОСТЬ =', error, '\n')

start()