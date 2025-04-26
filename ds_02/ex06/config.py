import os

# Файл логов
LOG_FILE = "analytics.log"

# Количество предсказаний
num_of_steps = 3

# Шаблон отчёта
report_template = """\
Report
We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively.
Our prediction is that in the next {steps} observations we will have: {pred_tails} tails and {pred_heads} heads.
"""

# Telegram API
TELEGRAM_BOT_TOKEN = "7669266906:AAE9stnjsufHb1q7_hHVViI4f8PrLGcx9bI"
TELEGRAM_CHAT_ID = "961376908"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
