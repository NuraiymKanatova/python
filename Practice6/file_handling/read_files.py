from pathlib import Path

file_path = Path("file_handling/data/sample.txt")

if not file_path.exists():
    print("File does not exist. Run write_files.py first.")
else:
    # r = read
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("Using read():")
        print(content)

    with open(file_path, "r", encoding="utf-8") as file:
        print("Using readline():")
        print(file.readline().strip())
        print(file.readline().strip())

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Using readlines():")
        for line in lines:
            print(line.strip())