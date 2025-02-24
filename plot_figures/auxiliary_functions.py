import numpy as np


def find_index_positive(data_x, data_y, index_number):
    index1 = np.where(data_x >= 0)[0][0]

    if index_number == 1:
        return index1
    elif index_number == 2:
        indexes2 = np.where(data_y[index1:len(data_y)] == 0)[0]

        if len(indexes2 > 0):
            index2 = indexes2[0]
        else:
            index2 = len(data_y) - 1

        return index2
    else:
        raise Exception("Index number must be 1 or 2.")


def number_bins(data, width_bins):
    return int((max(data) - min(data)) / width_bins)
