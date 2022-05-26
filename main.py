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
        #table = pd.read_excel('examlpe5.xlsx')

        # x
        hz = table.values[:, 1]

        # y
        l_spectrum = table.values[:, 5]
        r_spectrum = table.values[:, 9]

        # одномерный массив
        hz_new = np.linspace(hz.min(), hz.max(), 200)

        # k = 3 - кубический сплайн
        spl_l = interpolate.make_interp_spline(hz, l_spectrum, k=3)
        spl_r = interpolate.make_interp_spline(hz, r_spectrum, k=3)
        spl_spectrum_l = spl_l(hz_new)
        spl_spectrum_r = spl_r(hz_new)

        # Простое скользящее среднее
        arr_x = table.values[:, 1]
        arr_y_r = table.values[:, 5]
        arr_y_l = table.values[:, 9]
        window_size = 15
        
        i = 0
        # Initialize an empty list to store moving averages
        moving_averages_x = []
        moving_averages_y_r = []
        moving_averages_y_l = []
        
        # Loop through the array t o
        #consider every window of size 3
        while (i < len(arr_x) - window_size + 1) & (i < len(arr_y_l) - window_size + 1) & (i < len(arr_y_r) - window_size + 1):
        
            # Calculate the average of current window
            window_average_x = round(np.sum(arr_x[i:i+window_size]) / window_size, 2)
            window_average_y_r = round(np.sum(arr_y_r[i:i+window_size]) / window_size, 2)
            window_average_y_l = round(np.sum(arr_y_l[i:i+window_size]) / window_size, 2)

            # Store the average of current
            # window in moving average list
            moving_averages_x.append(window_average_x)
            moving_averages_y_r.append(window_average_y_r)
            moving_averages_y_l.append(window_average_y_l)

            # Shift window to right by one position
            i += 1

        
        # Convert array of integers to pandas series
        numbers_series_x2 = pd.Series(arr_x)
        numbers_series_y_r2 = pd.Series(arr_y_r)
        numbers_series_y_l2 = pd.Series(arr_y_r)
        
        # Get the moving averages of series
        # of observations till the current time
        moving_averages_x2 = round(numbers_series_x2.ewm(alpha=0.1, adjust=False).mean(), 2)
        moving_averages_y_r2 = round(numbers_series_y_r2.ewm(alpha=0.1, adjust=False).mean(), 2)
        moving_averages_y_l2 = round(numbers_series_y_l2.ewm(alpha=0.1, adjust=False).mean(), 2)

        # Convert pandas series back to list
        moving_averages_list_x2 = moving_averages_x2.tolist()
        moving_averages_list_y_r2 = moving_averages_y_r2.tolist()
        moving_averages_list_y_l2 = moving_averages_y_l2.tolist()


    # отрисовка данных
        # plot l_spectrum
        plt.subplot(2, 4, 1)
        
        # initial date
        plt.plot(hz, l_spectrum, color='r')
        plt.grid()
        plt.ylabel("l_spectrum")
        plt.xlabel("Исходные данные")

        # interpolation
        #plt.plot(hz_new, l_spectrum_new (hz_new), '--',  color='b')

        # splain
        plt.subplot(2, 4, 2)
        plt.plot(hz_new, spl_spectrum_l, '--',  color='b')
        plt.grid()
        plt.xlabel("Кубический сплайн")

        # skolz
        plt.subplot(2, 4, 3)
        plt.plot(moving_averages_x, moving_averages_y_r, '--',  color='b')
        plt.grid()
        plt.xlabel("Простое скользящее среднее, n = 15")

        # eps
        plt.subplot(2, 4, 4)
        plt.plot(moving_averages_x2, moving_averages_y_r2, '--',  color='b')
        plt.grid()
        plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")

        # plot r_tremor
        #
        #
        plt.subplot(2, 4, 5)

        # initial date
        plt.plot(hz, r_spectrum, color='r')
        plt.grid()
        plt.ylabel("r_spectrum")
        plt.xlabel("Исходные данные")

        # interpolation
        #plt.plot(time_new, r_tremor_new (time_new), '--',  color='b')

        # splain
        plt.subplot(2, 4, 6)
        plt.plot(hz_new, spl_spectrum_r, '--',  color='b')
        plt.grid()
        plt.xlabel("Кубический сплайн")

        plt.subplot(2, 4, 7)
        plt.plot(moving_averages_x, moving_averages_y_l, '--',  color='b')
        plt.grid()
        plt.xlabel("Простое скользящее среднее, n = 15")

        plt.subplot(2, 4, 8)
        plt.plot(moving_averages_x2, moving_averages_y_l2, '--',  color='b')
        plt.grid()
        plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")

        plt.show()
    
if __name__ == "__main__":
	main()