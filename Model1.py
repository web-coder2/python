import numpy as np
import matplotlib.pyplot as plt

while True:
	print("Зависимость электропроводности от температуры в проводниках")
	print("U = 5 Voltage; T0 = 20(deg of C);")
	print("---------------------------------")

	ro = float(input("ro удельное сопротивление проводника (Ohm*m^2/m) >>> "))
	l = float(input("длина проводника (м) >>> "))
	s = float(input("площадь поперченого сечения проводника (m^2) >>> "))

	alfa = float(input("температурный коэфициент сопротивления >>> "))
	t_end = float(input("T_end (C) >>> "))

	U = 5
	t0 = 20

	R = ro * l / s
	t_array = []
	r_array = []
	i_array = []

	while t0 <= t_end:
	  total_R = R + (R * alfa * t0)
	  total_i = U / total_R 
	  i_array.append(total_i)
	  r_array.append(total_R)
	  t_array.append(t0)
	  t0 += 1

	plt.figure(figsize=(6, 6)) 

	plt.subplot(2, 1, 1)
	plt.plot(t_array, r_array)
	plt.xlabel("Температуры (C)")
	plt.ylabel("Cопротивление (Ом)")
	plt.title("Зависимость сопротивления проводника от температуры")

	plt.subplot(2, 1, 2)
	plt.plot(t_array, i_array)
	plt.xlabel("Температуры (C)")
	plt.ylabel("Ток (А)")
	plt.title("Зависимость тока от температуры")

	plt.tight_layout()
	plt.show()
