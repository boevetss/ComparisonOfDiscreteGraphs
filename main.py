import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

table = pd.read_excel('examlpe.xlsx')
time_x = table.values[:, 0]
l_correl_y = table.values[:, 1]

# сглаживание графика
#x_int = np.linspace(time_x[0], l_correl_y[-1], 10)
#par = interpolate.splrep(time_x, l_correl_y, k = 3, s = 100)
#y_int = interpolate.splev(x_int, par, der = 0)

# сглаживание
inerp_graph = interpolate.interp1d(time_x, l_correl_y, kind='cubic')
xnew = np.linspace(time_x[0], time_x[len(time_x) - 1], 30)

# l_spectrum
plt.subplot(2, 1, 1)
plt.plot(time_x, l_correl_y, 'ro',xnew, inerp_graph(xnew), '--')
plt.plot(time_x, l_correl_y, marker = 'o', color='r')
plt.grid()
plt.xlabel("time")
plt.ylabel("l_spectrum")

# r_spectrum
plt.subplot(2, 1, 2)
plt.plot(time_x, l_correl_y, 'ro',xnew, f2(xnew), '--')
plt.plot(time_x, l_correl_y, marker = 'o', color='r')
plt.grid()
plt.xlabel("time")
plt.ylabel("r_spectrum")
plt.show()

