from pathlib import Path

# create a folder for demo files
data_dir = Path("file_handling/data")
data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir / "sample.txt"

# w = write (creates file if not exists, overwrites if exists)
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Line 1: Python file handling example\n")
    file.write("Line 2: Writing data to a file\n")

print("File created and initial data written.")

# a = append
with open(file_path, "a", encoding="utf-8") as file:
    file.write("Line 3: This line was appended\n")
    file.write("Line 4: Appending more data\n")

print("New lines appended.")

# x = create only fails if file already exists
new_file_path = data_dir / "new_file.txt"
try:
    with open(new_file_path, "x", encoding="utf-8") as file:
        file.write("This file was created using x mode.\n")
    print(f"{new_file_path} created successfully.")
except FileExistsError:
    print(f"{new_file_path} already exists.")