import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import integrate
import numpy as np

def main ():
    table = pd.read_excel('examlpe.xlsx')
    # x
    time = table.values[:, 0]
    # y
    l_tremor = table.values[:, 1]
    r_tremor = table.values[:, 2]

    time_new = np.linspace(time.min(), time.max(), 200) 
    spl_l = interpolate.make_interp_spline(time, l_tremor, k=3)
    spl_r = interpolate.make_interp_spline(time, r_tremor, k=3)
    spl_tremor_l = spl_l(time_new)
    spl_tremor_r = spl_r(time_new)

    area_l = integrate.trapz(spl_tremor_l, x = time_new)
    print(area_l)

    area_r = integrate.trapz(spl_tremor_r, x = time_new)
    print(area_r)

    # plot l_tremor
    #
    #
    plt.subplot(2, 1, 1)
    # initial date
    plt.plot(time, l_tremor, color='r')
    # interpolation
    #plt.plot(time_new, l_tremor_new (time_new), '--',  color='b')
    # splain
    plt.plot(time_new, spl_tremor_l, '--',  color='b')
    plt.grid()
    plt.ylim(-130, 130)
    plt.xlabel("time")
    plt.ylabel("l_tremor")
    plt.legend(['date', 'splain'])

    # plot r_tremor
    #
    #
    plt.subplot(2, 1, 2)
    # initial date
    plt.plot(time, r_tremor, color='r')
    # interpolation
    #plt.plot(time_new, r_tremor_new (time_new), '--',  color='b')
    # splain
    plt.plot(time_new, spl_tremor_r, '--',  color='b')
    plt.grid()
    plt.ylim(-130, 130)
    plt.xlabel("time")
    plt.ylabel("r_tremor")
    plt.legend(['data', 'splain'])

    plt.show()

if __name__ == "__main__":
	main()