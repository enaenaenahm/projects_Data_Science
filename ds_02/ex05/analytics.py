import os
import csv
from random import randint

class Research:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Error: data.csv not found")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        with open(self.file_path, newline='', encoding='utf-8') as file:
            reader = list(csv.reader(file))

            if len(reader) < 2 or len(reader[0]) != 2:
                raise ValueError("Error: Invalid CSV file header structure")

            if has_header:
                reader = reader[1:]

            data = []
            for row in reader:
                if row not in [["0", "1"], ["1", "0"]]:
                    raise ValueError("Error: Incorrect data in file")
                data.append([int(row[0]), int(row[1])])

            return data

class Calculations:

    def __init__(self, data):
        self.data = data

    def counts(self):
        heads_tails = sum(1 for row in self.data if row == [0, 1])
        tails_heads = sum(1 for row in self.data if row == [1, 0])
        return heads_tails, tails_heads

    def fractions(self, heads_tails, tails_heads):
        total = heads_tails + tails_heads
        return ((heads_tails / total) * 100, (tails_heads / total) * 100) if total else (0, 0)

class Analytics(Calculations):

    @staticmethod
    def predict_random(n):
        return [[randint(0, 1), 1 - randint(0, 1)] for _ in range(n)]

    def predict_last(self):
        return self.data[-1] if self.data else None

    @staticmethod
    def save_file(data, filename, extension="txt"):
        filepath = f"{filename}.{extension}"
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(data)
