import csv

class Must_read:
    file_path = "data.csv"  

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(",".join(row))  

