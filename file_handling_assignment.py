try:
    # File Creation
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("First line of text\n")
        file.write("Second line with numbers: 12345\n")
        file.write("Third line with special characters: !@#$%\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("Fourth line added in append mode\n")
        file.write("Fifth line appended with numbers: 67890\n")
        file.write("Sixth line appended with special characters: *&^(){}\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution completed.")
