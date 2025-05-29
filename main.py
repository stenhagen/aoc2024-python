from p1 import *
from p2 import *  
import re

def get_problem(problem_string):
    problem_func_mapping = {
        "1a" : p1a,
        "1b" : p1b,
        "2a" : p2a,
        "2b" : p2b
    }

    return problem_func_mapping[problem_string]

def main():
    print("Welcome to Adevent of Code 2024!")
    problem_to_run = '-1'
    while True:  
        print("What problem do you want to run on the form 1a, 1b, 2a? Type 0 to exit. Append 't' to test")
        problem_to_run = input().strip()
        if problem_to_run == '0':
            break
        try:
            p = r"^(\d{1,2}[ab])(t?)"
            m = re.match(p, problem_to_run)
            is_test = m.group(2) == 't'
            res = get_problem(m.group(1))(is_test)
            print(f"The problem result is {res}")
        except (KeyError):
            print("You are trying to run a task that doesn't exist") 

    print("You chose to end! Bye Bye!")

if __name__ == "__main__":
    main()