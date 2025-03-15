# Code to write samples to a file

# Sample file code - 01
# Writing to a file
# with open("sample_file_write.txt", "w") as file:
#     file.write("Hello World!")
def f1_write_file():
    with open("sample_file_write_01.txt", "w") as file:
        file.write("Hello World!")

print("\n01. Running function f1_write_file")
f1_write_file()

# Sample file code - 02
# Write lines to a file
# with open("sample_file_write.txt", "w") as file:
#     file.writelines(["Allice", "Bob", "Charlie"])
def f2_write_lines():
    with open("sample_file_write_02.txt", "w") as file:
        file.write("Hello World!\n")
        file.writelines(["Allice\n", "Bob\n", "Charlie\n"]) # This will write the lines with new line character

print("\n02. Running function f2_write_lines")
f2_write_lines()

# Sample file code - 03
# Append to a file
# with open("sample_file_write.txt", "a") as file:
#     file.write("Hello World!")
def f3_append_file():
    with open("sample_file_write_03.txt", "a") as file: # Note the mode "a" - append
        file.write("Hello World!")

print("\n03. Running function f3_append_file")
f3_append_file()


# Sample file code - 04
# Append lines to a file
# with open("sample_file_write.txt", "a") as file:
#     file.writelines(["Allice", "Bob", "Charlie"])
def f4_append_lines():
    with open("sample_file_write_04.txt", "a") as file: # Note the mode "a" - append
        file.write("Hello World!\n")
        file.writelines(["Allice\n", "Bob\n", "Charlie\n"]) # This will write the lines with new line character

print("\n04. Running function f4_append_lines")
f4_append_lines()

# Sample file code - 05
# Append to a file
# with open("sample_file_write.txt", "a") as file:
#     file.write("Hello World!")
def f5_append_file():
    with open("sample_file_write_05.txt", "a") as file: # Note the mode "a" - append
        file.write("Hello World!")

print("\n05. Running function f5_append_file")
f5_append_file()