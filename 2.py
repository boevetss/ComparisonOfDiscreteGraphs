import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Задаем параметры выборки
fs = 1000  # частота дискретизации, Гц
duration = 10  # длительность выборки, секунды

# Генерируем случайный белый шум
t = np.arange(0, duration, 1/fs)
noise = np.random.randn(len(t))

# Фильтруем шум, чтобы получить спектр тремора рук
b, a = signal.butter(4, [4, 16], btype='band', fs=fs)
tremor = signal.filtfilt(b, a, noise)

# Нормируем выборку
tremor = tremor / np.max(np.abs(tremor))

# Визуализируем спектр тремора
freq, psd = signal.welch(tremor, fs=fs, nperseg=1024)
plt.plot(freq, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD')
plt.show()