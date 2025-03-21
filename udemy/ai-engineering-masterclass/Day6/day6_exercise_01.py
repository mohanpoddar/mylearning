import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
print("Script Location:", script_directory)

# Define the output file path in the same directory as the script
output_file_path = os.path.join(script_directory, "day6_exercise_01_execution_explanation.txt")

# Open the output file for writing
with open(output_file_path, "w") as explanation_file:

    # Write the introduction to the explanation file
    explanation_file.write("Step-by-Step Execution Explanation of day6_exercise_01.py\n")
    explanation_file.write("=" * 60 + "\n\n")

    # Step 1: Define the function
    explanation_file.write("Step 1: Define the function `count_words_and_lines`\n")
    explanation_file.write(
        "This function takes a file path as input, reads the file, counts the number of lines, "
        "and calculates the total number of words in the file.\n\n"
    )

    def count_words_and_lines(file_path):
        explanation_file.write("Step 2: Open the file and read its contents\n")
        explanation_file.write(
            f"Opening the file at path: {file_path}\n"
        )
        file = open(file_path)
        lines = file.readlines()
        file.close()
        explanation_file.write(
            f"File read successfully. Total lines read: {len(lines)}\n"
        )

        word_count = 0
        for line in lines:
            words = line.split()
            word_count += len(words)
        explanation_file.write(
            f"Total words counted in the file: {word_count}\n\n"
        )
        return len(lines), word_count

    # Step 3: Try block to execute the main logic
    explanation_file.write("Step 3: Enter the try block to execute the main logic\n")
    try:
        file_path = 'udemy/ai-engineering-masterclass/Day6/sample_file_read.txt'
        explanation_file.write(
            f"File path set to: {file_path}\n"
        )

        # Step 4: Call the function
        explanation_file.write("Step 4: Call the `count_words_and_lines` function\n")
        lines, words = count_words_and_lines(file_path)
        explanation_file.write(
            f"Function returned: Number of lines = {lines}, Number of words = {words}\n\n"
        )

        # Step 5: Print the results
        explanation_file.write("Step 5: Print the results\n")
        explanation_file.write(
            f"Number of lines: {lines}\n"
            f"Number of words: {words}\n\n"
        )

    # Step 6: Handle exceptions
    except NameError as e:
        explanation_file.write("Step 6: Handle NameError exception\n")
        explanation_file.write(f"Error encountered: {e}\n\n")

    except FileNotFoundError as e:
        explanation_file.write("Step 6: Handle FileNotFoundError exception\n")
        explanation_file.write(f"Error encountered: {e}\n\n")

    except SyntaxError as e:
        explanation_file.write("Step 6: Handle SyntaxError exception\n")
        explanation_file.write(f"Error encountered: {e}\n\n")

    except Exception as e:
        explanation_file.write("Step 6: Handle generic exceptions\n")
        explanation_file.write(f"Error encountered: {e}\n\n")

    # Step 7: Finally block
    finally:
        explanation_file.write("Step 7: Execute the finally block\n")
        explanation_file.write("The finally block is always executed, regardless of whether an exception occurred.\n\n")

    # End of explanation
    explanation_file.write("=" * 60 + "\n")
    explanation_file.write("End of Execution Explanation\n")
    explanation_file.write("=" * 60 + "\n")

print(f"Execution explanation saved to {output_file_path}")
