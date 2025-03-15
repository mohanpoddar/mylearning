# Description: This file contains the sample code for reading a file in python

# Sample file content - 01
# Reading a file
# with open("sample_file_read.txt", "r") as file:
#     content = file.read()
#     print(content)
def f1_read_file():
    with open("sample_file_read.txt", "r") as file:
        content = file.read()
        print(content)

print("\n01. Running function f1_read_file")    
f1_read_file()

# Sample file content - 02
# Read line
# with open("sample_file_read.txt", "r") as file:
#     content = file.readline()
#     print(content)
def f2_read_line():
    with open("sample_file_read.txt", "r") as file:
        content = file.readline()   # Read the first line
        print(content)
        content = file.readline()  # Read the second line
        print(content)
        content = file.readline()  # Read the third line
        print(content)

print("\n02. Running function f2_read_file")  
f2_read_line()

# Sample file content - 03
# Read all lines
# with open("sample_file_read.txt", "r") as file:
#     content = file.readlines()
#     print(content)
def f3_read_all_lines():
    with open("sample_file_read.txt", "r") as file:
        content = file.readlines()
        print(content) # This wll print all the lines in the file
        print(content[2]) # This will print the third line in the file
        print(content[2][0]) # This will print the first character of the third line

print("\n03. Running function f3_read_file")  
f3_read_all_lines()

# Sample file content - 04
# Read all lines using for loop
# with open("sample_file_read.txt", "r") as file:
#     for line in file:
#         print(line)
def f4_read_all_lines_using_for_loop():
    with open("sample_file_read.txt", "r") as file:
        for line in file:
            print(line)

print("\n04. Running function f4_read_all_lines_using_for_loop")
f4_read_all_lines_using_for_loop()

# Sample file content - 05
# Read all lines using for loop and strip
# with open("sample_file_read.txt", "r") as file:
#     for line in file:
#         print(line.strip())
def f5_read_all_lines_using_for_loop_and_strip():
    with open("sample_file_read.txt", "r") as file:
        for line in file:
            print(line.strip()) # This will remove the new line character at the end of the line

print("\n05. Running function f5_read_all_lines_using_for_loop_and_strip")
f5_read_all_lines_using_for_loop_and_strip()

# Sample file content - 06
# Read all lines using for loop and split
# with open("sample_file_read.txt", "r") as file:
#     for line in file:
#         print(line.split())
def f6_read_all_lines_using_for_loop_and_split():
    with open("sample_file_read.txt", "r") as file:
        for line in file:
            print(line.split()) # This will split the line into words

print("\n06. Running function f6_read_all_lines_using_for_loop_and_split")
f6_read_all_lines_using_for_loop_and_split()

# Sample file content - 07
# Read all lines using for loop and split
# with open("sample_file_read.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         print(words)
def f7_read_all_lines_using_for_loop_and_split():
    with open("sample_file_read.txt", "r") as file:
        for line in file:
            words = line.split()
            print(words)   # This will split the line into words
            print(words[0]) # This will print the first word
            print(words[1]) # This will print the second word

print("\n07. Running function f7_read_all_lines_using_for_loop_and_split")
f7_read_all_lines_using_for_loop_and_split()

# Sample file content - 08
def f8_read_all_lines_using_for_loop_and_split(word_indices=None):
    """
    Reads all lines from a file, splits them into words, and prints specific words based on indices.

    Args:
        word_indices (list): List of indices of words to print from each line. If None, prints all words.
    """
    with open("sample_file_read.txt", "r") as file:
        for line in file:
            words = line.split()
            print("All words:", words)  # Print all words in the line
            print(len(words)) # Print the number of words in the line
            print(words[0]) # Print the first word in the line
            print(word_indices) # Print the word indices to print
            if word_indices: # Check if word_indices is not None
                for index in word_indices:
                    print(f"Word at index {index}:", words[index])
                    if index < len(words):  # Check if the index is valid
                        print(f"Word at index {index}:", words[index])

print("\n08. Running function f8_read_all_lines_using_for_loop_and_split")
f8_read_all_lines_using_for_loop_and_split(word_indices=[0, 1])  # Example: Print the first and third words