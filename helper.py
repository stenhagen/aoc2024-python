import os
 
def read_full_file(file_name, is_test = False, dir=None):
    data_folder = "real" if not is_test else "test"
    data_path = os.path.join(os.getcwd(), "data", data_folder, file_name) if dir is None else os.path.join(dir, file_name)
    try: 
        with open(data_path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"The file {data_path} you are attempting to read doesn't exist")
        return "n/a"
    
def read_lines_file(file_name, is_test = False, dir=None):
    data_folder = "real" if not is_test else "test"
    data_path = os.path.join(os.getcwd(), "data", data_folder, file_name) if dir is None else os.path.join(dir, file_name)
    try: 
        with open(data_path) as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"The file {data_path} you are attempting to read doesn't exist")
        return "n/a"