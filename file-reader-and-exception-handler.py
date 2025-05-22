# Get the filename from the user
filename = input("Enter the filename to read: ")

try:
    # Attempt to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except IOError as e:
    print(f"An I/O error occurred while reading the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # Modify the content (convert to uppercase)
    modified_content = content.upper()
    
    # Generate the new filename by appending '_modified.txt'
    parts = filename.rsplit('.', 1)
    if len(parts) > 1:
        new_filename = f"{parts[0]}_modified.{parts[1]}"
    else:
        new_filename = f"{filename}_modified.txt"
    
    try:
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"File successfully modified and saved as '{new_filename}'.")
    except IOError as e:
        print(f"Error writing to file '{new_filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")
