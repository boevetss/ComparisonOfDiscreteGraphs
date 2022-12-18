import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import integrate
import numpy as np
from tkinter import *
from sklearn import metrics
from statistics import mean

def main ():
    # выделение диапазонов
        def _palki(step, graph, color):
            ax.axvspan(step - 2, step, color = color, alpha = 0.4)
            
        def mnogo_palok(ax):
            _palki(2, ax, "red")
            _palki(4, ax, "orange")
            _palki(6, ax, "yellow")
            _palki(8, ax, "yellow")
            _palki(10, ax, "green")
            _palki(12, ax, "#4DA6FF")
            _palki(14, ax, "blue")

    # обработка данных
        # для примера используется файл с измерениями P1_2 
        #table = pd.read_excel('examlpe.xlsx')
        table = pd.read_excel('examlpe5.xlsx')

        # x
        hz = table.values[:, 1]

        # y
        l_spectrum = table.values[:, 5]
        r_spectrum = table.values[:, 9]

        # одномерный массив
        hz_new = np.linspace(hz.min(), hz.max(), int(len(hz) / 4))

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

        # init date
        plt.subplot(2, 4, 1)
        plt.plot(hz, l_spectrum, color='r')
        plt.grid()
        plt.ylabel("l_spectrum")
        plt.xlabel("Исходные данные")

        # splain
        ax = plt.subplot(2, 4, 2)
        #ymin, ymax = plt. ylim()
        plt.plot(hz_new, spl_spectrum_l, '--',  color='b')
        mnogo_palok(ax)
        plt.grid()
        plt.xlabel("Кубический сплайн")

        # skolz
        ax = plt.subplot(2, 4, 3)
        plt.plot(moving_averages_x, moving_averages_y_r, '--',  color='b')
        mnogo_palok(ax)
        plt.grid()
        plt.xlabel("Простое скользящее среднее, n = 15")

        # eps
        ax = plt.subplot(2, 4, 4)       
        plt.plot(moving_averages_x2, moving_averages_y_r2, '--',  color='b')
        mnogo_palok(ax)
        plt.grid()
        plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")

        # plot r_tremor
        

        # initial date
        plt.subplot(2, 4, 5)
        plt.plot(hz, r_spectrum, color='r')
        plt.grid()
        plt.ylabel("r_spectrum")
        plt.xlabel("Исходные данные")

        # splain
        ax = plt.subplot(2, 4, 6)
        mnogo_palok(ax)
        plt.plot(hz_new, spl_spectrum_r, '--',  color='b')
        plt.grid()
        plt.xlabel("Кубический сплайн")

        # skolz
        ax = plt.subplot(2, 4, 7)
        mnogo_palok(ax)
        plt.plot(moving_averages_x, moving_averages_y_l, '--',  color='b')
        plt.grid()
        plt.xlabel("Простое скользящее среднее, n = 15")

        # eps
        ax = plt.subplot(2, 4, 8)
        mnogo_palok(ax)
        plt.plot(moving_averages_x2, moving_averages_y_l2, '--',  color='b')
        plt.grid()
        plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")

        plt.show()

        error_hz = []
        for el in hz_new:
            error_hz.extend([el, el, el, el])


    # оценка точности
        # среднняя абсолютная ошибка
        print(f'Средняя абсолютная ошибка (по модулю) = {metrics.mean_absolute_error(error_hz, hz)}')

        # среднеквадратическая ошибка MSE
        #print(f'Средний квадрат ошибки (квадрат) = {metrics.mean_squared_error(error_hz, hz)}')

        # среднеквадратическая ошибка RMSE
        print(f'Среднеквадратическая ошибка = {np.sqrt(metrics.mean_squared_error(error_hz, hz))}')
    
    # сравнение диапазонов
    # диапазоны 0-2 и 6-8
    # нахождение среднего на диапазонах и их сравнение
        # диапазоны 0_2 и 6_8
        list_0_2 = []
        for i in range(len(l_spectrum)):
            if (hz[i] > 0) and (hz[i] < 2):
                list_0_2.append(l_spectrum[i])
        #print(list_0_2)
        list_avg_0_2 = mean (list_0_2)
        #print(list_avg_0_2)

        list_4_6 = []
        for i in range(len(l_spectrum)):
            if (hz[i] > 4) and (hz[i] < 6):
                list_4_6.append(l_spectrum[i])
        #print(list_0_2)
        list_avg_4_6 = mean (list_4_6)
        #print(list_avg_4_6)

        list_7_10 = []
        for j in range(len(l_spectrum)):
            if (hz[j] > 7) and (hz[j] < 10):
                list_7_10.append(l_spectrum[j])
        #print(list_6_8)
        list_avg_7_10 = mean (list_7_10)
        #print(list_avg_7_10)

        list_12_14 = []
        for i in range(len(l_spectrum)):
            if (hz[i] > 12) and (hz[i] < 14):
                list_12_14.append(l_spectrum[i])
        #print(list_0_2)
        list_avg_12_14 = mean (list_12_14)
        #print(list_avg_12_14)

        if list_avg_0_2 > list_avg_7_10:
            print("Пациент здоров!")
        else: 
            print("Пациент не здоров!")

        list = [list_avg_0_2, list_avg_4_6, list_avg_7_10]
        list_min = min(list)
        list_max = max (list)

        if list_min == list_avg_4_6:
            print("Пациент здоров!")
        else: 
            print("Пациент не здоров!")

        if list_max == list_avg_0_2:
            print("Пациент здоров!")
        else: 
            print("Пациент не здоров!") 

        if list_avg_7_10 > list_avg_12_14:
            print("Пациент здоров!")
        else: 
            print("Пациент не здоров!")  

        if list_avg_0_2 > list_avg_4_6 and list_avg_7_10 > list_avg_12_14:
            print("Пациент здоров!")
        else: 
            print("Пациент не здоров!")     
  
if __name__ == "__main__":
	main()