def write_to_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
            print("File 'my_file.txt' created and written successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")
    finally:
        print("File creation process completed.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")

def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("Appending line 1\n")
            file.write("78910\n")
            file.write("Another line for appending\n")
            print("Content appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")

if __name__ == "__main__":
    filename = "my_file.txt"

    #write to file
    write_to_file(filename)

    #Read to file
    read_from_file(filename)

    #append to file
    append_to_file(filename)
