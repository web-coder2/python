import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


# здесь будут разные функции для физических систем (механика электрика магнетизм и т.д.) 
def basic_derivative():
    timeRange = float(input("input timeRange for modelling >>>"))
    timeDelta = float(input("input delta of timeItem in t(sec) >>>"))
    function_str = input("input function f(x) [x(t), v(t) and others] >>>") 
    resultList = []

    def function(x):
        return eval(function_str)

    time_points = np.linspace(0, timeRange, int(timeRange / timeDelta) + 1)
    dfdx = [derivative(function, x, dx=timeDelta) for x in time_points]

    print("dfdx:", dfdx)

    plt.plot(time_points, dfdx)
    plt.xlabel("Время (сек)")
    plt.ylabel("Производная")
    plt.title("График производной")
    plt.show()


def LR_electric():
    timeRange = float(input("input timeRange for modelling >>>"))
    timeDelta = float(input("input delta of timeItem in t(sec) >>>"))
    time_points = np.linspace(0, timeRange, int(timeRange / timeDelta) + 1)

    i0 = float(input("i0(Am) >>>"))
    R = float(input("R(Om) >>>"))
    L = float(input("L(Hn) >>>"))

    # I = i0 * exp(-t*R / L)

    current = i0 * np.exp(-time_points * R / L)
    heat = R * np.cumsum(current**2 * timeDelta) 

    # Строим график
    plt.plot(time_points, current)
    plt.xlabel("Время (с)")
    plt.ylabel("Ток (А)")
    plt.title("Изменение тока в LR цепи")
    plt.grid(True)
    plt.show()

    plt.plot(time_points, heat)
    plt.xlabel("Время (с)")
    plt.ylabel("Теплота (Дж)")
    plt.title("Накопление теплоты на резисторе")
    plt.grid(True)
    plt.show()


# что то своего рода main menu  и запуск разных вещей
while True:
    print("1) derivative x(t) v(t) or I(q)")
    print("2) LR electric circuit")
    mode = int(input("select a physics system >>> "))

    if mode == 1:
	    basic_derivative()
    if mode == 2:
        LR_electric()