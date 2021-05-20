import math
import numpy as np
def count_novel(text):

    arr_text = text.split()
    single = []
    c = np.zeros(len(arr_text))
    cnt = 0
    for i in range(len(arr_text)):
        if not (single.__contains__(arr_text[i])):
            single.append(arr_text[i])
            cnt += 1
        c[i] = cnt

    return c
