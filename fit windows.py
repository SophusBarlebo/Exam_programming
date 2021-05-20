import math
import numpy as np
def fit_windows(b, w, side):

    height = math.floor(b[2]/w[1])
    length = math.floor(b[0]/w[0])
    width = math.floor(b[1]/w[0])

    if side == 'length':
        c = 2 * length * height
    elif side == 'width':
        c = 2 * width * height
    else:
        c = (2 * length * height) + (2 * width * height)

    return c
