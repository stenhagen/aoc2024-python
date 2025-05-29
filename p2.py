from helper import *
import re
import numpy as np
from functools import partial

def is_report_safe_standard(report):
    report_orig = np.array([int(n) for n in (report + [0])[1:-1]])
    report_shifted_right = np.array([int(n) for n in ([0] + report)[1:-1]])
    diffs = np.subtract(report_orig, report_shifted_right)
    min_diff = diffs.min()
    max_diff = diffs.max()
    is_safe = (min_diff >= 1 and max_diff <= 3) or (min_diff >= -3 and max_diff <= -1)
    return is_safe 

def remove_index(report, index):
    return report[:index] + report[index + 1:]

def is_report_safe_dampener_extended(report):
    """
    Adds dampener extension functionality by removing one index one by one 
    and see if any of the reduced reports passes
    """
    if is_report_safe_standard(report):
        return True
    is_any = sum([1 for ind in range(len(report)) if is_report_safe_standard(remove_index(report, ind))]) > 0
    return is_any
    
def p2a(is_test=False, test_file_name="2t.txt"):
    file_name = "2r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    reports = [l.split() for l in lines]
    nof_safe_reports = sum([1 for r in reports if is_report_safe_standard(r)])
    return nof_safe_reports

def p2b(is_test=False, test_file_name="2t.txt"):
    file_name = "2r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    reports = [l.split() for l in lines]
    nof_safe_reports = sum([1 for r in reports if is_report_safe_dampener_extended(r)])
    return nof_safe_reports