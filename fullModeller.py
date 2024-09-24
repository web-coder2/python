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

    print("time_points:", time_points)
    print("dfdx:", dfdx)

    plt.plot(time_points, dfdx)
    plt.xlabel("Время (сек)")
    plt.ylabel("Производная")
    plt.title("График производной")
    plt.show()


# что то своего рода main menu  и запуск разных вещей
while True:
	print("-------------------------------")
	print("1) derivative x(t) v(t) or I(q)")
	mode = int(input("select a physics system >>> "))
	print("-------------------------------")

	if mode == 1:
		basic_derivative()
