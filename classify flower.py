import math
import numpy as np

def classify_flower(D, q):

    copied = np.copy(D)
    for j in range(len(q) - 1):
        for i in range(len(D[:, 0])):
            if q[j] == 0:
                i = i
            elif not (q[j] == D[i][j]):
                copied[i][j] = -1

    for i in range(len(D[:, 0])):
        if not(-1 in copied[i]):
            copied[i][len(q) - 1] = abs(copied[i][len(q) - 1] - q[len(q) - 1])

    sum = -1
    for i in range(len(D[:, 0])):
        if (not(-1 in copied[i])) and (copied[i][len(q) - 1]) > sum:
            c = np.array([i+1, 1])

    return c
