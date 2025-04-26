import sys
import config
from analytics import Research, Analytics

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        data = research.file_reader()
        analytics = Analytics(data)

        heads_tails, tails_heads = analytics.counts()
        perc_heads_tails, perc_tails_heads = analytics.fractions(heads_tails, tails_heads)
        predictions = analytics.predict_random(config.num_of_steps)

        pred_tails = sum(1 for row in predictions if row == [1, 0])
        pred_heads = sum(1 for row in predictions if row == [0, 1])

        report = config.report_template.format(
            total=len(data),
            tails=tails_heads,
            heads=heads_tails,
            tails_pct=perc_tails_heads,
            heads_pct=perc_heads_tails,
            steps=config.num_of_steps,
            pred_tails=pred_tails,
            pred_heads=pred_heads
        )

        analytics.save_file(report, "report")

        print("The report has been saved to 'report.txt'.")
        Research.send_telegram_message("The report has been successfully created")

    except ValueError as e:
        print(e)
        Research.send_telegram_message("The report hasn’t been created due to an error")
        sys.exit(1)

if __name__ == "__main__":
    main()
