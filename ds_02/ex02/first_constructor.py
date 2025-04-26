import csv
import sys
import os

class Research:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Error: data.csv not found")
        self.file_path = file_path

    def file_reader(self):
        try:
            with open(self.file_path, newline='', encoding='utf-8') as file:
                reader = list(csv.reader(file))
                return [",".join(row) for row in reader]
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: data.csv not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]  
    research = Research(file_path)

    for line in research.file_reader():
        print(line)

