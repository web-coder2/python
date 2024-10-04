import os 
try:
	import pandas as pd
	import numpy as np 
	import matplotlib.pyplot as plt
except:
	os.system("pip install pandas numpy matplotlib")
	import pandas as pd
	import numpy as np 
	import matplotlib.pyplot as plt 	  


data = pd.read_csv("plot-data.csv")
print(data.head(6)) # first 6 rows of data
print(data.columns)

x = data["x"]
y = data[" y"]

while True:
	print("degress this is summ of K(i) * x(i)  + b")
	degree = int(input("input number of degrees >>> "))
	_coeffs = np.polyfit(x, y, degree)
	polinomial = np.poly1d(_coeffs)

	start_x = int(input("input start for x new array >>> "))
	end_x = int(input("input end for x new array >>> "))
	nums_x = int(input("input number x new array >>> "))

	new_x_array = np.linspace(start_x, end_x, nums_x)
	new_y_array = polinomial(new_x_array)

	plt.plot(new_x_array, new_y_array)
	plt.xlabel("x data")
	plt.ylabel("y data")
	plt.title("coeffs => " + str(_coeffs))
	plt.show()