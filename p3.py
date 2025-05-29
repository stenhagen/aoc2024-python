from helper import *
import re
import numpy as np
from functools import partial

def p3a(is_test=False, test_file_name="3t.txt"):
    file_name = "3r.txt" if not is_test else test_file_name 
    content = read_full_file(file_name, is_test)
    if content == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    mul_pairs = re.findall(pattern, content)
    multiplied = [int(m[0]) * int(m[1]) for m in mul_pairs]
    return sum(multiplied)