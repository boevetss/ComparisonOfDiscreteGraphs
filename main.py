import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

table = pd.read_excel('D://study//leti//vkr_mag//examlpe.xlsx')
time = table.values[:, 0]
l_tremor = table.values[:, 1]
r_tremor = table.values[:, 2]

# сглаживание графика
#x_int = np.linspace(time_x[0], l_correl_y[-1], 10)
#par = interpolate.splrep(time_x, l_correl_y, k = 3, s = 100)
#y_int = interpolate.splev(x_int, par, der = 0)

# сглаживание
# l_tremor
l_tremor_new = interpolate.interp1d(time, l_tremor, kind='cubic')
# r_tremor
r_tremor_new = interpolate.interp1d(time, r_tremor, kind='cubic')
# time
time_new = np.linspace(time[0], time[len(time) - 1], 80)

# plot l_tremor
plt.subplot(2, 1, 1)
# initial date
plt.plot(time, l_tremor, color='r')
# interpolation
plt.plot(time_new, l_tremor_new (time_new), '--',  color='b')
plt.grid()
plt.xlabel("time")
plt.ylabel("l_tremor")

# plot r_tremor
plt.subplot(2, 1, 2)
# initial date
plt.plot(time, r_tremor, color='r')
# interpolation
plt.plot(time_new, r_tremor_new (time_new), '--',  color='b')
plt.grid()
plt.xlabel("time")
plt.ylabel("r_tremor")
plt.show()