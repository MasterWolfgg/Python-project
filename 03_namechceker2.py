import tkinter as tk

# Function to check if a name is present in the text file
def check_name_in_file(name, file_name):
    with open(file_name, 'r') as file:
        for line in file:
            if name.lower() in line.lower():
                return True
    return False

# Function to handle the name checking process
def check_name():
    name_to_check = entry.get()
    if name_to_check.lower() == 'q':
        result_label.config(text="Goodbye!")
        return

    if check_name_in_file(name_to_check, file_name):
        result_label.config(text=f"{name_to_check} is present in the file.")
    else:
        result_label.config(text=f"{name_to_check} is not present in the file.")
    
# Create the main window
root = tk.Tk()
root.title("Name Checker GUI")

# Label and Entry for user input
instruction_label = tk.Label(root, text="Enter a name to check (or 'q' to quit):")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

# Button to initiate the check
check_button = tk.Button(root, text="Check Name", command=check_name)
check_button.pack()

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack()

file_name = 'names.txt'  # Change this to your text file's name

root.mainloop()
