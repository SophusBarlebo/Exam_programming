import numpy as np
import math

def qualify(A, R):

    score_list = np.zeros(int(A.size)).astype(int)

    for i in range(len(A[:, 0])):
        if R[i][0] == R[i][1]:
            score_list[A[i][0] - 1] += 1
            score_list[A[i][1] - 1] += 1
        elif R[i][0] > R[i][1]:
            score_list[A[i][0] - 1] += 2
            score_list[A[i][1] - 1] += 0
        elif R[i][0] < R[i][1]:
            score_list[A[i][0] - 1] += 0
            score_list[A[i][1] - 1] += 2

    score = score_list.tolist()
    t = np.zeros(2)
    for i in range(2):
        t[i] = score.index(max(score)) + i + 1
        score.remove(max(score))

    return t
