import os
# Count words and lines in a text file

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "sample_file_read.txt")
print("Script Location:", script_directory)
print("File Path:", file_path)

def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines_count = len(lines)
            
            # List comprehension
            # l = [len(line.split()) for line in lines]
            # print(f"{l}")
            # print(sum(l))
            word_count = sum(len(line.split()) for line in lines)
            
            # Using for loop
            word_count = 0
            for line in lines:
                word_count += len(line.split())
      
            print(f"Number of lines: {lines_count}")
            print(f"Numbers of words using list comprehension: {word_count}")
            print(f"Number of words using loop: {word_count}")

    except NameError as e:
        print(f"Error: {e}")
    
    except AttributeError as e:
        print(f"Error: {e}")

    except SyntaxError as e:
        print(f"Error: {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

count_words_and_lines(file_path)