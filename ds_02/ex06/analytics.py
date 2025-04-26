import os
import csv
import logging
import requests
from random import randint
import config

# Настройка логирования
logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class Research:
    def __init__(self, file_path):
        """Принимает путь к файлу."""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Ошибка: файл '{file_path}' не найден.")
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

    @staticmethod
    def send_telegram_message(message):
        payload = {
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": message,
        }
        response = requests.post(config.TELEGRAM_API_URL, json=payload)
        return response.status_code == 200

class Calculations:

    def __init__(self, data):
        self.data = data

    def counts(self):
        logging.info("We calculate the number of heads and tails")
        heads_tails = sum(1 for row in self.data if row == [0, 1])
        tails_heads = sum(1 for row in self.data if row == [1, 0])
        return heads_tails, tails_heads

    def fractions(self, heads_tails, tails_heads):
        logging.info("We calculate the probabilities of heads and tails")
        total = heads_tails + tails_heads
        return ((heads_tails / total) * 100, (tails_heads / total) * 100) if total else (0, 0)

class Analytics(Calculations):

    @staticmethod
    def predict_random(n):
        logging.info(f"Generate {n} random predictions")
        return [[randint(0, 1), 1 - randint(0, 1)] for _ in range(n)]

    def predict_last(self):
        return self.data[-1] if self.data else None

    @staticmethod
    def save_file(data, filename, extension="txt"):
        logging.info(f"Save data to a file: {filename}.{extension}")
        filepath = f"{filename}.{extension}"
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(data)
