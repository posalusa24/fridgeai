from os import path
import csv
from datetime import datetime, timedelta


def list():
    with open(path.join("data", "inventory.csv"), newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row['label'] for row in reader]


def add(label):
    with open(path.join("data", "inventory.csv"), "a", newline="") as csvfile:
        fieldnames = [
            'id',
            'label',
            'initial_date',
            'best_before',
            'quantity'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'id': 0,
            'label': label,
            'initial_date': str(datetime.today()),
            'best_before': str(datetime.today() + timedelta(days=3)),
            'quantity': 1
        })
