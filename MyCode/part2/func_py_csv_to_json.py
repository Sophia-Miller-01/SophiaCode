# func_py_csv_to_json.py
import csv
import json

def func_py_csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

func_py_csv_to_json("data.csv", "data.json")
