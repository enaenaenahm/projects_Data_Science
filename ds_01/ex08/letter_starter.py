import sys

def letter_starter(email):
    try:
        with open('employees.tsv', 'r') as tsv_file:
            lines = tsv_file.readlines()
            for line in lines[1:]:  
                line = line.strip()
                if not line:  
                    continue

                parts = line.split('\t')
                if len(parts) != 3:  
                    continue  
                name, surname, e = parts
                if e == email:
                    print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                    return
            print("Email not found")
    except FileNotFoundError:
        print("Error: File 'employees.tsv' not found.")
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python letter_starter.py <email>")
    else:
        letter_starter(sys.argv[1])