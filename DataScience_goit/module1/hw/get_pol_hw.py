import numpy as np


def get_polynom(coords):
    len_points = len(coords) - 1

    a = np.zeros((len_points + 1, len_points + 1))
    for row, coord in enumerate(coords):
        for ind in range(len(coords)):
            a[row][ind] = coord[0] ** len_points
            len_points -= 1
        len_points = len(coords) - 1

    b = np.array([coord[1] for coord in coords]).reshape(len_points + 1, 1)

    return np.linalg.solve(a, b)


print(get_polynom([(1, 12), (3, 54), (-1, 2), (5, 123), (7, 234)]))
