def modify_file_content(input_filename, output_filename):
    try:
        # Open the input file and read its contents
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was a problem reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input and output file names
input_filename = input("Enter the name of the file to read from: ")
output_filename = input("Enter the name of the file to write to: ")

# Call the function to perform the file read and write operations
modify_file_content(input_filename, output_filename)
