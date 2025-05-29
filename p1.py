from helper import *
import re

def p1a(is_test=False, test_file_name="1t.txt"):
    file_name = "1r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    pattern = r"^(\d+)\s+(\d+)$"
    pairs_orig = [re.match(pattern, l).group(1, 2) for l in lines]
    left_ordered = sorted([int(p[0]) for p in pairs_orig])
    right_ordered = sorted([int(p[1]) for p in pairs_orig])
    distance = sum([abs(p[0] - p[1]) for p in zip(left_ordered, right_ordered)])
    return distance