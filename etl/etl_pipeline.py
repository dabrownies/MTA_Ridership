import csv
from datetime import datetime

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

def clean_column_name(col_name):
    """Convert to lowercase snake_case"""
    return col_name.strip().lower().replace(":", "").replace("-", "").replace(" ", "_")

def transform_data(headers, rows):
    """Clean and transform the extracted ridership data."""
    cleaned_rows = []

    # clean headers
    cleaned_headers = [clean_column_name(col) for col in headers]

    for row in rows:
        cleaned_row = {}

        for key, value in row.items():
            clean_key = clean_column_name(key)

            # clean date field
            if clean_key == "date":
                try:
                    cleaned_date = datetime.strptime(value.strip(), "%m/%d/%Y").strftime("%Y-%m-%d")
                    cleaned_row[clean_key] = cleaned_date
                except ValueError:
                    cleaned_row[clean_key] = None

            # clean ridership numbers
            elif "ridership" in clean_key or "trips" in clean_key or "traffic" in clean_key:
                try:
                    cleaned_row[clean_key] = int(value.replace(",", ""))
                except:
                    cleaned_row[clean_key] = 0  # fallback

            # keep other fields as-is
            else:
                cleaned_row[clean_key] = value.strip()

        cleaned_rows.append(cleaned_row)

    return cleaned_headers, cleaned_rows

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

    cleaned_headers, cleaned_rows = transform_data(headers, rows)

    print("Cleaned headers:", cleaned_headers)
    print("Sample cleaned row:", cleaned_rows[0])