import csv
import os

DATA_DIR = "data"
OUTPUT_FILE = "output.csv"

def process_file(file_path, writer):
    with open(file_path, newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for product, raw_price, quantity, date, region in reader:
            if product == "pink morsel":
                price = float(raw_price[1:])
                sale = price * int(quantity)
                writer.writerow([sale, date, region])

def main():
    with open(OUTPUT_FILE, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["sales", "date", "region"])
        for file_name in os.listdir(DATA_DIR):
            process_file(os.path.join(DATA_DIR, file_name), writer)

if __name__ == "__main__":
    main()
