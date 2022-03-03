import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import integrate
import numpy as np
from tkinter import *

def main ():
    # обработка данных
        # для примера используется файл с измерениями P1_2 
        table = pd.read_excel('examlpe.xlsx')

        # x
        time = table.values[:, 0]

        # y
        l_tremor = table.values[:, 1]
        r_tremor = table.values[:, 2]
        # l_spectrum = table.values[:, 3]
        # r_spectrum = table.values[:, 4]

        # одномерный массив
        time_new = np.linspace(time.min(), time.max(), 200)

        # k = 3 - кубический сплайн
        spl_l = interpolate.make_interp_spline(time, l_tremor, k=3)
        spl_r = interpolate.make_interp_spline(time, r_tremor, k=3)
        spl_tremor_l = spl_l(time_new)
        spl_tremor_r = spl_r(time_new)

        # вычисление интеграла
        area_l = integrate.trapz(spl_tremor_l, x = time_new)
        print(area_l)
        area_r = integrate.trapz(spl_tremor_r, x = time_new)
        print(area_r)

    # отрисовка данных
        # plot l_tremor
        plt.subplot(2, 2, 1)
        
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
        plt.subplot(2, 2, 3)

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

        # шаблон для левой руки
        plt.subplot(2, 2, 2)
        plt.plot(time, l_tremor, color='r')
        plt.grid()
        plt.ylim(-130, 130)
        plt.xlabel("time")
        plt.ylabel("l_tremor")

        # шаблон данных для правой руки
        plt.subplot(2, 2, 4)
        plt.plot(time, r_tremor, color='r')
        plt.grid()
        plt.ylim(-130, 130)
        plt.xlabel("time")
        plt.ylabel("r_tremor")

        plt.show()
    
if __name__ == "__main__":
	main()