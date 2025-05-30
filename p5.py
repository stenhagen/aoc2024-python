from helper import *
import re

def get_last_rule_break_comp_index(rules, selected, rest_of_line):
    """
    Finds the latest index of any value in rest_of_line breaking a rule with regards to selected
    """
    rule_breaks = [np.where(np.array(rest_of_line) == int(r[0])) for r in rules if int(r[1]) == selected and int(r[0]) in rest_of_line]
    return max(rule_breaks[0][0]) if len(rule_breaks) > 0 else -1

def is_update_line_correct(rules, line):
    """
    is_update_line_correct() works recursively to determine whether the line is correct given the rules.
    In every recursive iteration the line is left-stripped by one.
    """
    # If the length of line is 1 then the line is correct 
    if len(line) == 1:
        return True
    selected = line[0]
    rest_of_line = line[1:]
    # If selected doesn't violate rules given its successing comparators then rerun is_update_line_correct()
    # stepping selected one index forward
    if get_last_rule_break_comp_index(rules, selected, rest_of_line) == -1:
        return is_update_line_correct(rules, rest_of_line)
    else:
        return False

def order_incorrect_line(rules, line, select_index):
    """
    order_incorrect_line() is a recursive function that orders line according to rules.
    In each call select_index marks the index of the number currently under scrutiny. 
    No lower indides than select_index will ever be swapped.
    """
    # If select_index is at end of line, the lines has been successfully ordered.  
    if select_index == len(line) - 1:
        return line
    selected = line[select_index]
    rest_of_line = line[select_index + 1:]
    # Get the last index of any comparator that makes selected fail 
    last_comp_index = get_last_rule_break_comp_index(rules, selected, rest_of_line)
    if last_comp_index == -1: # If no such index exist incrememt select index
        return order_incorrect_line(rules, line, select_index + 1)
    else:
        # If a rule break index exist. Swap selected and the number at the rule break index
        # and rerun with same select_index.
        line[select_index], line[select_index + 1 + last_comp_index] = line[select_index + 1 + last_comp_index], line[select_index]
        return order_incorrect_line(rules, line, select_index)
    
def p5a(is_test=False, test_file_name="5t.txt"):
    file_name = "5r.txt" if not is_test else test_file_name 
    lines = read_lines_file(file_name, is_test)
    if lines == "n/a":
        print("The file wasn't found, can't run task. Returning")
        return
    delim = lines.index('\n')
    rules_pattern = r"^(\d+)\|(\d+)$"
    rules = lines[:delim] 
    rule_pairs = [re.match(rules_pattern, r).group(1,2) for r in rules] # Rule pairs as list of tuples
    update_lines_str = lines[delim + 1:]
    update_lines = [[int(n) for n in s.strip().split(',')] for s in update_lines_str]
    correct_lines = [l for l in update_lines if is_update_line_correct(rule_pairs, l)]
    sum_of_middle_index = sum([l[len(l)//2] for l in correct_lines])
    return sum_of_middle_index

def p5b(is_test=False, test_file_name="5t.txt"):
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
    incorrect_orig_lines = [l for l in update_lines if not is_update_line_correct(rule_pairs, l)]
    corrected_lines = [order_incorrect_line(rule_pairs, l, 0) for l in incorrect_orig_lines]
    sum_of_middle_index = sum([l[len(l)//2] for l in corrected_lines])
    return sum_of_middle_index
