import csv

class Research:
    file_path = "data.csv" 

    def file_reader(self):
        try:
            with open(self.file_path, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return [",".join(row) for row in reader] 
        except FileNotFoundError:
            return ["Error: data.csv not found"]

if __name__ == "__main__":
    research = Research()
    for line in research.file_reader():
        print(line)
