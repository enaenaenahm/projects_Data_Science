import sys
import os

def names_extractor(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open('employees.tsv', 'w') as tsv_file:
        tsv_file.write("Name\tSurname\tE-mail\n")
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 3: 
                print(f"Skipping invalid line: {line}")
                continue
            name, surname, email = parts
            email = email.strip()
            if '.' in email and '@' in email:
                tsv_file.write(f"{name.capitalize()}\t{surname.capitalize()}\t{email}\n")
            else:
                print(f"Skipping invalid email format: {email}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <file_path>")
    else:
        names_extractor(sys.argv[1])