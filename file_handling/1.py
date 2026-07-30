"""
method_option             purpose
r                         read file  if not found return error
w                         overwrite in  existing file or create file or write
a                         append in the last line or create it
x                         create fails if already exists
t                         text mode (by default)
b                         binary mode (rb , wb)
+                         read and write (r+,w+, a+)

"""

import functools
from functools import wraps

def file_handler(mode, encoding="utf-8"):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            file_path = kwargs.pop("filepath", None)

            if file_path is None and args:
                file_path = args[0]
                args = args[1:]

            if file_path is None:
                raise ValueError("File path is required")

            with open(file_path, mode, encoding=encoding) as file_obj:
                return func(file_obj, *args, **kwargs)

        return wrapper

    return decorator


def file_reading(filepath:str, line_limit:int=10):
     with open(filepath,'r') as f:
         print(f)
         print(f.read())
         print("reading line by line")
         for i in range(line_limit):
             line=f.readline()
             if not line:
                 break
             print(line)

@file_handler(mode='r')
def file_reading_using_decorator(file_obj, line_limit: int = 10):
        print(file_obj)
        print(file_obj.read())
        print("reading line by line")
        for i in range(line_limit):
            line = file_obj.readline()
            if not line:
                break
            print(line)

def file_writing(filepath: str):
    with open(filepath, 'w') as f:
        f.write("hello2 world ")

def write_file_using_w(filepath:str):
    with open(filepath,'a+') as f:
        print(f)
        file_input=input("Enter a string")
        f.write(file_input)

        f.seek(0)
        print("reading file")
        print(f.read())
        print("using list of string")
        file_input_list=file_input.split()
        f.writelines(file_input_list)
        f.seek(0)
        print("reading file again")
        print(f.read())






if __name__=="__main__":
    file="hello.txt"
    print("file_reading function")
    file_reading(file)

    print("file writing")
    # file_writing(file)


    file_reading_using_decorator(file)
