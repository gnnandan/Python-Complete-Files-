import os 

def current_directory():
    cwd=os.getcwd()
    print(f"The current working directory is:{cwd}")
    print()
def file_path(filename):
    path = os.path.abspath(filename)
    print(f"The absolute path of file is:{path}")
    print()
    
current_directory()
filename="1_scripting.py"
file_path(filename)