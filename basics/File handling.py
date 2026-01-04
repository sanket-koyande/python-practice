# file_handling.py
# Demonstration of File Handling in Python

filename = "sample.txt"

# 1. Writing to a file
def write_file():
    with open(filename, "w") as file:
        file.write("Python File Handling\n")
        file.write("This file is created using write mode.\n")
    print("File written successfully.\n")

# 2. Reading from a file
def read_file():
    with open(filename, "r") as file:
        content = file.read()
        print("Reading file content:")
        print(content)

# 3. Appending to a file
def append_file():
    with open(filename, "a") as file:
        file.write("This line is appended to the file.\n")
    print("Data appended successfully.\n")

# 4. Reading file line by line
def read_line_by_line():
    with open(filename, "r") as file:
        print("Reading file line by line:")
        for line in file:
            print(line, end="")
    print()

# 5. Main execution
write_file()
append_file()
read_file()
read_line_by_line()
