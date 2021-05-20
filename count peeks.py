import numpy as np

def count_peaks(A):

    c = 0

    print(A)
    for i in range(len(A[:, 0])):
        for j in range(len(A[0, :])):
            print(c)

            if len(A[0, :]) == 1:
                if j == 0:
                    if A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
                elif j == len(A[:, 0]):
                    if A[i][j] >= (A[i][j - 1] + 2):
                        c += 1
                elif A[i][j] >= (A[i][j - 1] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                    c += 1
                else:
                    if A[i][j] >= (A[i][j - 1] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
            elif i == 0:
                if j == 0:
                    if A[i][j] >= (A[i + 1][j] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
                elif j == len(A[:, 0]) - 1:
                    if A[i][j] >= (A[i + 1][j] + 2) or A[i][j] >= (A[i][j - 1] + 2):
                        c += 1
                else:
                    if A[i][j] >= (A[i + 1][j] + 2) or A[i][j] >= (A[i][j - 1] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
            elif i == len(A[0, :]):
                if j == 0:
                    if A[i][j] >= (A[i - 1][j] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
                elif j == len(A[:, 0]):
                    if A[i][j] >= (A[i - 1][j] + 2) or A[i][j] >= (A[i][j - 1] + 2):
                        c += 1
                else:
                    if A[i][j] >= (A[i - 1][j] + 2) or A[i][j] >= (A[i][j - 1] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                        c += 1
            else:
                if A[i][j] >= (A[i + 1][j] + 2) or A[i][j] >= (A[i - 1][j] + 2) or A[i][j] >= (A[i][j - 1] + 2) or A[i][j] >= (A[i][j + 1] + 2):
                    c += 1

    return c


import numpy as np
print(count_peaks(np.reshape([1,2,3,5,3,7,7.1,3,3,3,4,4,7,7.3], [2, 7])))