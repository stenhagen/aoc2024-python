from helper import *
import re
import numpy as np
from functools import partial

def p3a(is_test=False, test_file_name="3ta.txt"):
    file_name = "3r.txt" if not is_test else test_file_name 
    content = read_full_file(file_name, is_test)
    if content == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    mul_pairs = re.findall(pattern, content)
    multiplied = [int(m[0]) * int(m[1]) for m in mul_pairs]
    return sum(multiplied)

def is_mul_enabled(do_positions, dont_positions, mul_position):
    # Artifically adding matches at position -1 for do() and -2 for don't()
    # to ensure default when wnetering string is always do()
    do_pos_np = np_int_array([-1] + do_positions)
    do_pos_filter = max(do_pos_np[do_pos_np < mul_position])
    dont_pos_np = np_int_array([-2] + dont_positions)
    dont_pos_filter = max(dont_pos_np[dont_pos_np < mul_position])
    return do_pos_filter > dont_pos_filter
    

def p3b(is_test=False, test_file_name="3tb.txt"):
    file_name = "3r.txt" if not is_test else test_file_name 
    content = read_full_file(file_name, is_test)
    if content == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    do_pattern = r"do\(\)"
    do_matches = list(re.finditer(do_pattern, content))
    do_positions = [m.span()[0] for m in do_matches] 
    dont_pattern = r"don't\(\)"
    dont_matches = list(re.finditer(dont_pattern, content))
    dont_positions = [m.span()[0] for m in dont_matches]
    
    mul_pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    mul_matches = list(re.finditer(mul_pattern, content))
    f = partial(is_mul_enabled, do_positions, dont_positions)
    multiplied = [int(m.group(1)) * int(m.group(2)) for m in mul_matches if f(m.span()[0])]
    return sum(multiplied)