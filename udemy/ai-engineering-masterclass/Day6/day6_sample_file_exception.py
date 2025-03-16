# Write code for file exception handling
#
# # Sample file code - 01 FileNotFoundError
# # Writing code for file exception handling
# Raised when the specified file does not exist.
# def f1_file_exception_handling():\
def f1_file_exception_handling():
    try:
        with open("sample_file_read_for_exception.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("Some other error occurred")
        print(e)    
    finally:
        print("Finally block is always executed")

print("\n01. Running function f1_file_exception_handling")
f1_file_exception_handling()

# # Sample file code - 02 PermissionError
# # Writing code for file exception handling for /etc/shadow file for permission denied
# Raised when the program does not have the required permissions to access the file (e.g., trying to read shadow without root privileges).
# def f2_file_exception_handling():
def f2_file_exception_handling():
    try:
        with open("/etc/shadow", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("Some other error occurred")
        print(e)    
    finally:
        print("Finally block is always executed")

print("\n02. Running function f2_file_exception_handling")
f2_file_exception_handling()

# # Sample file code - 03 IsADirectoryError
# # Writing code for file exception handling for directory
# Raised when attempting to open a directory as if it were a file.
# def f3_file_exception_handling():
def f3_file_exception_handling():
    try:
        with open("/etc", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except IsADirectoryError:
        print("Cannot open a directory as a file")   
    finally:
        print("Finally block is always executed")

print("\n03. Running function f3_file_exception_handling")
f3_file_exception_handling()

# # Sample file code - 04 IOError (or OSError)
# # Writing code for file exception handling for IOError
# A more general error that occurs when an I/O operation fails (e.g., disk issues, file system errors).
# def f4_file_exception_handling():
def f4_file_exception_handling():
    try:
        with open("/etc/shadow", "r") as file:
            content = file.read()
            print(content)
    except IOError:
        print("Input/Output error")    
    finally:
        print("Finally block is always executed")

print("\n04. Running function f4_file_exception_handling")
f4_file_exception_handling()

# # Sample file code - 05 ValueError
# # Writing code for file exception handling for ValueError
# Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
# Raised when an invalid mode is passed to the open() function (e.g., invalid file mode like "invalid_mode").
# def f5_file_exception_handling():
def f5_file_exception_handling():
    try:
        with open("sample_file_read.txt", "r") as file:
            content = file.read()
            print(int(content))
    except ValueError:
        print("Value error")

    finally:
        print("Finally block is always executed")

print("\n05. Running function f5_file_exception_handling")
f5_file_exception_handling()

# # Sample file code - 06 ZeroDivisionError
# # Writing code for file exception handling for ZeroDivisionError
# def f6_file_exception_handling():
def f6_file_exception_handling():
    try:
        num = 10
        divisor = 0
        result = num / divisor
        print(result)
    except ZeroDivisionError:
        print("Zero division error")
    finally:
        print("Finally block is always executed")
   
print("\n06. Running function f6_file_exception_handling")
f6_file_exception_handling()


# # Sample file code - 07 ZeroDivisionError
# # Writing code for file exception handling for ZeroDivisionError
# def f7_file_exception_handling():
def f7_file_exception_handling(a, b):
    try:
        result = a / b
        print(f'Result: {result}')
    except ZeroDivisionError:
        print("Zero division error")
        
    finally:
        print("Finally block is always executed")

print("\n07. Running function f7_file_exception_handling")
f7_file_exception_handling(10, 5)
f7_file_exception_handling(10, 0)

# # Sample file code - 08 General Exception Handling
# # Writing code for file exception handling for General Exception Handling
# def f8_file_exception_handling():
def f8_file_exception_handling():
    try:
        with open("file_does_not_exit.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print("Error:", e)
   
    finally:
        print("Finally block is always executed")

print("\n08. Running function f8_file_exception_handling")
f8_file_exception_handling()
