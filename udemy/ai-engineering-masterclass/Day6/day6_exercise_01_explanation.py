import os

explanation = """
Unpacking the Return Values:

The returned values are unpacked into two variables:
1. lines: Stores the number of lines in the file.
2. words: Stores the total number of words in the file.

Detailed Explanation:
- The function `count_words_and_lines` returns a tuple `(len(lines), word_count)`.
- This tuple contains:
  - `len(lines)`: The total number of lines in the file.
  - `word_count`: The total number of words in the file.

Unpacking Example:
- Suppose the file contains:
  Hello world
  This is a test file

- The function will return `(2, 6)`:
  - `2`: Number of lines.
  - `6`: Number of words.

- These values are unpacked into:
  lines = 2
  words = 6

Why Unpacking is Useful:
- Readability: Makes the code cleaner and easier to understand.
- Efficiency: Avoids manual indexing into the tuple.
- Convenience: Assigns meaningful variable names to the returned values.

Summary:
- Unpacking allows the program to directly use the returned values for further processing or output.
"""

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output file path in the same directory as the script
output_file_path = os.path.join(script_directory, "day6_exercise_01_explanation.txt")

# Save the explanation to the output file
with open(output_file_path, "w") as file:
    file.write(explanation)

print(f"Explanation saved to {output_file_path}")