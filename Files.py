# 1. Write a program to read a text file
def read_text_file(filename):
    print("Reading text file:")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found")

# 2. Write a program to write text to .txt file using InputStream
def write_text_file(filename, text):
    print(f"Writing text to {filename}:")
    try:
        with open(filename, 'w') as file:
            file.write(text)
            print("Write successful")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

# 3. Write a program to read a file stream
def read_file_stream(filename):
    print("Reading file stream:")
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            print(content.decode('utf-8'))  # Decoding bytes to string for demonstration
    except FileNotFoundError:
        print(f"File {filename} not found")

# 4. Write a program to read a file stream that supports random access
def read_file_stream_random_access(filename):
    print("Reading file stream with random access:")
    try:
        with open(filename, 'rb+') as file:
            content = file.read()
            print(content.decode('utf-8'))  # Decoding bytes to string for demonstration
    except FileNotFoundError:
        print(f"File {filename} not found")

# 5. Write a program to read a file and jump to a particular index using seek()
def read_file_at_index(filename, index):
    print(f"Reading file from index {index}:")
    try:
        with open(filename, 'rb') as file:
            file.seek(index)
            content = file.read()
            print(content.decode('utf-8'))  # Decoding bytes to string for demonstration
    except FileNotFoundError:
        print(f"File {filename} not found")
    except IOError as e:
        print(f"Error reading from file {filename}: {e}")

# 6. Write a program to check whether a file has read access and write access permissions
def check_file_permissions(filename):
    import os
    print(f"Checking permissions for file {filename}:")
    try:
        read_access = os.access(filename, os.R_OK)
        write_access = os.access(filename, os.W_OK)
        
        if read_access:
            print(f"File {filename} has read access.")
        else:
            print(f"File {filename} does not have read access.")
        
        if write_access:
            print(f"File {filename} has write access.")
        else:
            print(f"File {filename} does not have write access.")
    except Exception as e:
        print(f"Error checking file permissions: {e}")

# Example usage of the above functions
filename = 'example.txt'

# Write some text to the file
write_text_file(filename, "Hello, this is a test file.")

# Read the text from the file
read_text_file(filename)

# Read the file stream
read_file_stream(filename)

# Read the file stream with random access
read_file_stream_random_access(filename)

# Read the file from a specific index
read_file_at_index(filename, 7)

# Check file permissions
check_file_permissions(filename)
