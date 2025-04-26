# Количество предсказаний
num_of_steps = 3

# Шаблон отчёта
report_template = """\
Report
We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively.
Our prediction is that in the next {steps} observations we will have: {pred_tails} tails and {pred_heads} heads.
"""
