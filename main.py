import pandas as pd
import matplotlib.pyplot as plt
from scipy import *
from scipy import interpolate
from scipy import integrate
import numpy as np
import metrics
from statistics import mean
from scipy.fft import fft, ifft
from scipy.fft import fft, fftfreq
from numpy.linalg import inv

def main ():
    def draw_graph(x, y_l, y_r, xfft_l, yfft_l, xfft_r, yfft_r, xspl_l, yspl_l, xspl_r, yspl_r, xpr, ypr_l, ypr_r, xexp, yexp_l, yexp_r, i):
        if i == 1:
            # 3.3.1 БПФ
            # Исходные данные. Левый спектр
            plt.subplot(2, 2, 1)
            plt.plot(x, y_l, color='r')
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("Исходные данные. Левый спектр") 

            # Исходные данные. Правый спектр
            plt.subplot(2, 2, 3)
            plt.plot(x, y_r, color='r')
            plt.grid()
            plt.ylabel("r_spectrum")
            plt.xlabel("Исходные данные. Правый спектр")

            # Исходные данные. БПФ. Левый спектр
            plt.subplot(2, 2, 2)
            plt.plot(xfft_l, yfft_l, color='r')
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("БПФ. Левый спектр") 

            # Исходные данные. БПФ. Правый спектр
            plt.subplot(2, 2, 4)
            plt.plot(xfft_r, yfft_r, color='r')
            plt.grid()
            plt.ylabel("r_spectrum")
            plt.xlabel("БПФ. Правый спектр")

            plt.show()

        if i == 2:
            # 3.3.1 Аппроксимация
            # Исходные данные. Левый спектр
            plt.subplot(2, 2, 1)
            plt.plot(x, y_l, color='r')
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("Исходные данные") 

            # Исходные данные. Правый спектр
            plt.subplot(2, 2, 3)
            plt.plot(x, y_r, color='r')
            plt.grid()
            plt.ylabel("r_spectrum")
            plt.xlabel("Исходные данные")

            # 3.3.1.1 
            # Спектр левой руки
            plt.subplot(2, 2, 2)
            plt.plot(xspl_l, yspl_l, color="r")
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("Аппроксимация полиномом 7 степени")
            #plt.ylim([-5, 125])
            #plt.ylim([0, 12])

            # Спектр правой руки
            plt.subplot(2, 2, 4)
            plt.plot(xspl_r, yspl_r, color="r")
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("Аппроксимация полиномом 7 степени")
            #plt.ylim([-5, 305])
            #plt.ylim([0, 8])

            plt.show()

        if i == 3:
             # 3.3.3. Скользящее среднее
            # Исходные данные. Спектр левой руки
            plt.subplot(2, 3, 1)
            plt.plot(x, y_l, color='r')
            plt.grid()
            plt.ylabel("l_spectrum")
            plt.xlabel("Исходные данные")

            # Исходные данные. Спектр правой руки
            plt.subplot(2, 3, 4)
            plt.plot(x, y_r, color='r')
            plt.grid()
            plt.ylabel("r_spectrum")
            plt.xlabel("Исходные данные")

            # 3.3.3.1 Простое скользящее среднее
            # Спектр левой руки
            ax = plt.subplot(2, 3, 2)
            plt.plot(xpr, ypr_l, '--',  color='b')
            plt.grid()
            plt.xlabel("Простое скользящее среднее, n = 15")
            #plt.ylim([-5, 125])
            #plt.ylim([0, 12])
            
            # Спектр правой руки
            ax = plt.subplot(2, 3, 5)
            plt.plot(xpr, ypr_r, '--',  color='b')
            plt.grid()
            plt.xlabel("Простое скользящее среднее, n = 15")
            #plt.ylim([-5, 305])
            #plt.ylim([0, 8])

            # 3.3.3.2 Экспоненциальное скользящее среднее
            # Спектр левой руки
            ax = plt.subplot(2, 3, 3)
            plt.plot(xexp, yexp_l, '--',  color='b')
            plt.grid()
            plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")
            #plt.ylim([-5, 125])
            #plt.ylim([0, 12])

            # Спектр правой руки
            ax = plt.subplot(2, 3, 6)       
            plt.plot(xexp, yexp_r, '--',  color='b')
            plt.grid()
            plt.xlabel("Экспон. скользящее среднее, альфа = 0.1")
            #plt.ylim([-5, 305])
            #plt.ylim([0, 8])

            plt.show()

    # анализ данных
    def analyse_data(hz, l_spectrum, r_spectrum, hz_ill, l_spectrum_ill, r_spectrum_ill):
        # БПФ
        """data_l = l_spectrum
        ly_l = np.fft.fft(data_l)
        freq_l = np.fft.fftfreq(len(ly_l), 30)
        x_l = np.abs(freq_l)
        y_l = np.abs(ly_l)

        data_r = l_spectrum
        ly_r = np.fft.fft(data_r)
        freq_r = np.fft.fftfreq(len(ly_r), 30)
        x_r = np.abs(freq_r)
        y_r = np.abs(ly_r)

        #def draw_graph(x, y_l, y_r, xfft_l, yfft_l, xfft_r, yfft_r, xspl_l, xspl_r, yspl_l, yspl_r, xpr, ypr_l, ypr_r, xexp, yexp_l, yexp_r, i):
        
        draw_graph(hz, l_spectrum, r_spectrum, x_l, y_l, x_r, y_r, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)"""
        
        # 1 Полиномиальная аппроксимация 
        def polynomial_regression(x, y, degree):
            n = len(x)
            X = np.zeros((n, degree + 1))
            for i in range(n):
                for j in range(degree + 1):
                    X[i][j] = x[i]**j
            Y = y.reshape(n, 1)
            Xt = np.transpose(X)
            XtX = np.dot(Xt, X)
            XtY = np.dot(Xt, Y)
            inv_XtX = inv(XtX)
            coef = np.dot(inv_XtX, XtY)
            return coef.flatten()
        
        def smooth_data(x, y, degree):
            coef = polynomial_regression(x, y, degree)
            smooth_y = np.zeros(len(x))
            for i in range(len(x)):
                for j in range(degree + 1):
                    smooth_y[i] += coef[j] * x[i]**j
            return smooth_y
    
        # 1. Полиномиальная аппроксимация
        """def polynom_date(hz, l_spectrum, r_spectrum):           
            pl3 = np.polyfit (hz, l_spectrum, 13)
            xxl = np.linspace (hz[0], hz[-1], len(hz))
            yyl3 = np.polyval(pl3, xxl)

            pr3 = np.polyfit (hz, r_spectrum, 13)
            xxr = np.linspace (hz[0], hz[-1], len(hz))
            yyr3 = np.polyval(pr3, xxr)

            #draw_graph(hz, l_spectrum, r_spectrum, 0, 0, 0, 0, xxl, yyl3, xxr, yyr3, 0, 0, 0, 0, 0, 0, 2)"""

        # 2. Cкользящее среднее
        def moving_average(hz, l_spectrum, r_spectrum):
            window_size = 15
                
            i = 0
            moving_averages_x = []
            moving_averages_y_r = []
            moving_averages_y_l = []
                
            #  Простое скользящее среднее
            # Loop through the array to consider every window of size 3
            while (i < len(hz) - window_size + 1) & (i < len(l_spectrum) - window_size + 1) & (i < len(r_spectrum) - window_size + 1):
                
                # Calculate the average of current window
                window_average_x = round(np.sum(hz[i:i+window_size]) / window_size, 2)
                window_average_y_r = round(np.sum(r_spectrum[i:i+window_size]) / window_size, 2)
                window_average_y_l = round(np.sum(l_spectrum[i:i+window_size]) / window_size, 2)

                # Store the average of current window in moving average list
                moving_averages_x.append(window_average_x)
                moving_averages_y_r.append(window_average_y_r)
                moving_averages_y_l.append(window_average_y_l)

                # Shift window to right by one position
                i += 1

            # Экспонениальное скользящее среднее
            # Convert array of integers to pandas series
            numbers_series_x2 = pd.Series(hz)
            numbers_series_y_r2 = pd.Series(r_spectrum)
            numbers_series_y_l2 = pd.Series(l_spectrum)
                
            # Get the moving averages of series of observations till the current time
            moving_averages_x2 = round(numbers_series_x2.ewm(alpha=0.1, adjust=False).mean(), 2)
            moving_averages_y_r2 = round(numbers_series_y_r2.ewm(alpha=0.1, adjust=False).mean(), 2)
            moving_averages_y_l2 = round(numbers_series_y_l2.ewm(alpha=0.1, adjust=False).mean(), 2)

            return  moving_averages_y_r,  moving_averages_y_l, moving_averages_y_l2,  moving_averages_y_r2

            #draw_graph (hz, l_spectrum, r_spectrum, 0, 0, 0, 0, 0, 0, 0, 0, moving_averages_x, moving_averages_y_l, moving_averages_y_r, moving_averages_x2, moving_averages_y_l2, moving_averages_y_r2, 3)
            
        # 3.1 Качественное сравнение
        def sravnenie(hz, spectrum_l, spectrum_r):
            def spectrum (hz, spectrum_l):
                index = 0
                index_ill = 0

                list_0_2 = []
                for i in range(len(spectrum_l)):
                    if (hz[i] > 0) and (hz[i] < 2):
                        list_0_2.append(spectrum_l[i])
                list_avg_0_2 = max (list_0_2)

                list_4_6 = []
                for i in range(len(spectrum_l)):
                    if (hz[i] > 4) and (hz[i] < 6):
                        list_4_6.append(spectrum_l[i])
                list_avg_4_6 = max (list_4_6)

                list_7_10 = []
                for j in range(len(spectrum_l)):
                    if (hz[j] > 7) and (hz[j] < 10):
                        list_7_10.append(spectrum_l[j])
                list_avg_7_10 = max (list_7_10)

                list_12_14 = []
                for i in range(len(spectrum_l)):
                    if (hz[i] > 12) and (hz[i] < 14):
                        list_12_14.append(spectrum_l[i])
                list_avg_12_14 = max (list_12_14)

                list = [list_avg_0_2, list_avg_4_6, list_avg_7_10]
                list_min = min(list)
                list_max = max (list)

                # самый главный критерий!
                if list_min == list_avg_4_6:
                    index += 1
                    parkinson = 'нет'
                else: 
                    index_ill += 1
                    parkinson = 'да'

                if list_avg_0_2 > list_avg_7_10:
                    index += 1
                else: 
                    index_ill += 1
            
                if list_max == list_avg_0_2:
                    index += 1
                else: 
                    index_ill += 1

                if list_avg_7_10 > list_avg_12_14:
                    index += 1
                else: 
                    index_ill += 1  

                if list_avg_0_2 > list_avg_4_6 and list_avg_7_10 > list_avg_12_14:
                    index += 1
                else: 
                    index_ill += 1

                return index, index_ill, parkinson

            spectr, spectr_ill, parkinson = spectrum(hz, spectrum_l)      
            
            diag_l = spectr * 2 * 10 
            diag_ill_l = spectr_ill * 2 * 10
            parkinson_l = parkinson

            spectr, spectr_ill, parkinson = spectrum(hz, spectrum_r)   

            diag_r = spectr * 2 * 10 
            diag_ill_r = spectr_ill* 2 * 10
            parkinson_r = parkinson

            if diag_l == diag_r and diag_ill_l == diag_ill_r and parkinson_l == parkinson_r:    
                print("Степень схожести c шаблоном графика здорого человека = ", diag_l, "%")
                print("Степень схожести c шаблоном графика человека с отклонениями в здоровье = ", diag_ill_l, "%")
                print("Наличие признаков Паркинсона (главный критерий схожести с шаблоном графика человека с отклонениями) - ", parkinson)

        # 3.2 Количественное сравнение. Алгоритм DTW
        def dtw(spectrum1, spectrum2, distance_func):
            n, m = len(spectrum1), len(spectrum2)
            dtw_matrix = np.zeros((n+1, m+1))
            dtw_matrix[1:, 0] = np.inf
            dtw_matrix[0, 1:] = np.inf
            for i in range(1, n+1):
                for j in range(1, m+1):
                    cost = distance_func(spectrum1[i-1], spectrum2[j-1])
                    dtw_matrix[i, j] = cost + min(dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])
            path = []
            i, j = n, m
            while i > 0 and j > 0:
                path.append((i-1, j-1))
                if dtw_matrix[i-1, j] < dtw_matrix[i, j-1]:
                    i -= 1
                else:
                    j -= 1
            return dtw_matrix[n, m], path[::-1]

        def euclidean_distance(x, y):
            return np.sqrt(np.sum((x - y) ** 2))
        
        # 3.3 Количественное сравнение. Критерий Пирсона
        
        # исходные данные
        smooth_yl = smooth_data(hz, l_spectrum, 13)
        smooth_yr = smooth_data(hz, r_spectrum, 13)
        draw_graph(hz, l_spectrum, r_spectrum, 0, 0, 0, 0, hz, smooth_yl, hz, smooth_yr, 0, 0, 0, 0, 0, 0, 2)
        
        # шаблон
        smooth_yl_ill = smooth_data(hz_ill, l_spectrum_ill, 13)
        smooth_yr_ill = smooth_data(hz_ill, r_spectrum_ill, 13)
        draw_graph(hz_ill, l_spectrum_ill, r_spectrum_ill, 0, 0, 0, 0, hz_ill, smooth_yl_ill, hz_ill, smooth_yr_ill, 0, 0, 0, 0, 0, 0, 2)
        #sravnenie(hz, l_spectrum, r_spectrum)

        sp1_l, sp1_r, spectrum1_l, spectrum1_r  = moving_average(hz, l_spectrum, r_spectrum)
        sp2_l, sp2_r, spectrum2_l, spectrum2_r = moving_average(hz_ill, l_spectrum_ill, r_spectrum_ill)
        
        print('Полиномиальная аппроксимация')
        distance, path = dtw(smooth_yl, smooth_yl_ill, euclidean_distance)
        print('Левая рука. DTW расстояние:', distance)
        distance, path = dtw(smooth_yr, smooth_yr_ill, euclidean_distance)
        print('Правая рука. DTW расстояние:', distance)
        
        print('Экспоненциальное скользящее среднее')
        distance, path = dtw(spectrum1_l, spectrum2_l, euclidean_distance)
        print('Левая рука. DTW расстояние:', distance)
        distance, path = dtw(spectrum1_r, spectrum2_r, euclidean_distance)
        print('Правая рука. DTW расстояние:', distance)

        print('Простое скользящее среднее')
        distance, path = dtw(sp1_l, sp2_l, euclidean_distance)
        print('Левая рука. DTW расстояние:', distance)
        distance, path = dtw(sp1_r, sp2_r, euclidean_distance)
        print('Правая рука. DTW расстояние:', distance)

        

    # качественное сравнение по диапазонам
    

        
    # обработка и нормализация данных
    def read_file():
        # для примера используется файл с измерениями P1_2 
        table = pd.read_excel('P5Sf_1.xlsx')
        pattern_ill = pd.read_excel('P5_3.xlsx')
        # транспонируем матрицу
        table = table.transpose()
        pattern_ill = pattern_ill.transpose()
        # частота (х)
        hz = table.values[1]
        hz_ill = pattern_ill.values[1]
        # спектры (у)
        l_spectrum = table.values[5]
        r_spectrum = table.values[9]
        l_spectrum_ill = pattern_ill.values[5]
        r_spectrum_ill = pattern_ill.values[9]

        analyse_data(hz, l_spectrum, r_spectrum, hz_ill, l_spectrum_ill, r_spectrum_ill)
    read_file()

if __name__ == "__main__":
	main()