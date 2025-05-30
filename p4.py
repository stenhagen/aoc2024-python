from helper import *
import re
import numpy as np
from functools import partial

def count_occurences_for_x(matrix, x_coord):
    env = matrix[x_coord[0] - 3: x_coord[0] + 4, x_coord[1] - 3: x_coord[1] + 4]
    left = ''.join(list(env[3, 3::-1]))
    upper = ''.join(list(env[3::-1, 3]))
    right = ''.join(list(env[3, 3:]))
    lower = ''.join(list(env[3:, 3]))
    upper_left_eye = np.pad(np.eye(4,4), ((0,3), (0,3)), 'constant', constant_values = 0)
    upper_left_mask = upper_left_eye == 1 
    upper_left = ''.join(list(env[upper_left_mask][::-1]))
    upper_right_eye = np.pad(np.fliplr(np.eye(4,4)), ((0, 3), (3,0)), 'constant', constant_values = 0)
    upper_right_mask = upper_right_eye == 1
    upper_right = ''.join(list(env[upper_right_mask][::-1]))
    lower_right_eye = np.pad(np.eye(4,4), ((3,0), (3,0)), 'constant', constant_values = 0)
    lower_right_mask = lower_right_eye == 1
    lower_right = ''.join(list(env[lower_right_mask]))
    lower_left_eye = np.pad(np.fliplr(np.eye(4,4)), ((3, 0), (0, 3)), 'constant', constant_values = 0)
    lower_left_mask = lower_left_eye == 1
    lower_left = ''.join(list(env[lower_left_mask]))
    dirs = [left, upper_left, upper, upper_right, right, lower_right, lower, lower_left]
    occurences = dirs.count("XMAS")
    return occurences


def p4a(is_test=False, test_file_name="4t.txt"):
    file_name = "4r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    lines_matrix = np.array([[c for c in line.strip()] for line in lines])
    padded_matrix = np.pad(lines_matrix, 3, 'constant', constant_values = ".")
    x_list = np.where(padded_matrix == 'X')
    x_pairs = zip(x_list[0], x_list[1])
    occurences = [count_occurences_for_x(padded_matrix, x_pos) for x_pos in x_pairs]
    total = sum(occurences)
    return total 