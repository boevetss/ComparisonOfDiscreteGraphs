import numpy as np

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

# пример использования
spectrum1 = np.array([1, 2, 3, 4, 5])
spectrum2 = np.array([1.2, 2.1, 3.2, 4.1, 5.2])
distance, path = dtw(spectrum1, spectrum2, euclidean_distance)
print('DTW расстояние:', distance)
print('DTW путь:', path)