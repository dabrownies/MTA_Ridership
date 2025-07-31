import csv
import requests
import codecs
import logging

def extract_csv(file_path):
    """Extract data from local MTA ridership CSV file."""
    all_rows = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, None)

        if headers is None:
            print("CSV is empty or improperly formatted.")
            return [], []

        for row in reader:
            if not row or len(row) != len(headers):
                continue
            row_dict = dict(zip(headers, row))
            all_rows.append(row_dict)

    return headers, all_rows

if __name__ == "__main__":
    CSV_PATH = "./data/mta_ridership.csv"
    headers, rows = extract_csv(CSV_PATH)

    print("Headers:\n-----------------------------")
    for field in headers:
        print(field)
    print("Sample row:\n-----------------------------")
    for field in rows[1]:
        print(field)
    print(f"Total rows: {len(rows)}")
