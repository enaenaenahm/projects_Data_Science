import sys
import os
import csv

class Research:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Error: data.csv not found")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        with open(self.file_path, newline='', encoding='utf-8') as file:
            reader = list(csv.reader(file))

            # Проверяем заголовок
            if len(reader) < 2 or len(reader[0]) != 2:
                raise ValueError("Error: Invalid CSV file header structure")

            # Убираем заголовок, если has_header=True
            if has_header:
                reader = reader[1:]

            # Проверяем данные и преобразуем в int
            data = []
            for row in reader:
                if row not in [["0", "1"], ["1", "0"]]:
                    raise ValueError("Error: Incorrect data in file")
                data.append([int(row[0]), int(row[1])])
            return data

    class Calculations:

        @staticmethod
        def counts(data):
            heads_tails = sum(1 for row in data if row == [0, 1])
            tails_heads = sum(1 for row in data if row == [1, 0])
            return heads_tails, tails_heads

        @staticmethod
        def fractions(heads_tails, tails_heads):
            total = heads_tails + tails_heads
            return ((heads_tails / total) * 100, (tails_heads / total) * 100) if total else (0, 0)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        data = research.file_reader()
        calculations = Research.Calculations()

        heads_tails, tails_heads = calculations.counts(data)
        perc_heads_tails, perc_tails_heads = calculations.fractions(heads_tails, tails_heads)

        print(data)  
        print(heads_tails, tails_heads)  
        print(perc_heads_tails, perc_tails_heads) 

    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
