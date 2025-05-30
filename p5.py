from helper import *
import re

def is_update_line_correct(rules, line):
    if len(line) == 1:
        return True
    selected = line[0]
    rest_of_line = line[1:]
    rule_breaks = [r for r in rules if int(r[1]) == selected and int(r[0]) in rest_of_line]
    if len(rule_breaks) == 0:
        return is_update_line_correct(rules, rest_of_line)
    else:
        return False

def p5a(is_test=False, test_file_name="5t.txt"):
    file_name = "5r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    delim = lines.index('\n')
    rules_pattern = r"^(\d+)\|(\d+)$"
    rules = lines[:delim]
    rule_pairs = [re.match(rules_pattern, r).group(1,2) for r in rules]
    update_lines_str = lines[delim + 1:]
    update_lines = [[int(n) for n in s.strip().split(',')] for s in update_lines_str]
    correct_lines = [l for l in update_lines if is_update_line_correct(rule_pairs, l)]
    sum_of_middle_index = sum([l[len(l)//2] for l in correct_lines])
    return sum_of_middle_index
    