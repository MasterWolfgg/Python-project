
def check_name_in_file(name, file_name):
    with open(file_name, 'r') as file:
        for line in file:
            if name.lower() in line.lower():
                return True
    return False


file_name = input("Enter the file name to check from ")

print("Welcome to the Name Checker Program! ")
print(f"Checking names in the file '{file_name}'.")

while True:
    name_to_check = input("Enter a name to check (or 'q' to quit): ")

    if name_to_check.lower() == 'q':
        print("Goodbye!")
        break

    if check_name_in_file(name_to_check, file_name):
        print(f"{name_to_check} is present in",file_name)
    else:
        print(f"{name_to_check} is not present in",file_name)
