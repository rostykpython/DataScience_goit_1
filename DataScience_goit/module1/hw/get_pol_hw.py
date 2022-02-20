import numpy as np


def get_polynom(coords):
    len_points = len(coords)

    a = np.zeros((len_points, len_points))
    b = np.zeros((len_points, 1))

    for row, coord in enumerate(coords):
        len_points -= 1
        for ind in range(len(coords)):
            a[row][ind] = coord[0] ** len_points
            len_points -= 1
        len_points = len(coords)
        b[row][0] = coord[1]
    return np.linalg.solve(a, b)


print(get_polynom([(1, 12), (3, 54), (-1, 2)]))
