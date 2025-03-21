import os
# Write and Read a List of Items

print("Script Absolute Path:", os.path.abspath(__file__))

script_directory = os.path.dirname(os.path.abspath(__file__))
print(f"Script Directory Path: {script_directory}")

output_file_path = os.path.join(script_directory, "day6_exercise_02_execution_explanation.txt")
print(f"Output File Path: {output_file_path}")

output_file_path = os.path.join(script_directory, "day6_exercise_02_output.txt")
print(f"Output File Path: {output_file_path}")

def write_list_to_file(output_file_path, items):
    try:
        with open(output_file_path, "w") as file:
            for item in items:
                file.write(f"{item}\n")
            print("List written to file successfully!")
            print("\nList items:")
            for item in items:
                print(item)
                
    except NameError as e:
        print(f"Error: {e}")
    
    except AttributeError as e:
        print(f"Error: {e}")
    
    except SyntaxError as e:
        print(f"Error: {e}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")

items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
write_list_to_file(output_file_path, items)

