import csv
import os

with open("tmp.csv", "w") as tmp_out:
    writer = csv.DictWriter(tmp_out, ['CIK', 'Ticker', 'Name'])
    writer.writeheader()

    with open("russell_2000_cik_to_ticker.csv", "r") as csv_in:
        reader = csv.DictReader(csv_in)
        for row in reader:
            writer.writerow(row)

    with open("missing_cik_ticker.csv", "r") as csv_in:
        reader = csv.DictReader(csv_in)
        for row in reader:
            writer.writerow(row)

os.rename("tmp.csv", "russell_2000_cik_to_ticker.csv")
