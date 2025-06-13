import csv
import os

FILE = 'sales.csv'
HEADERS = ['id', 'customer_name', 'product', 'quantity', 'price']

def setup_file():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()

def add_entry(entry):
    with open(FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(entry)

def show_entries():
    with open(FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def modify_entry(entry_id, new_data):
    records = []
    with open(FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] == entry_id:
                row.update(new_data)
            records.append(row)
    with open(FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(records)

def remove_entry(entry_id):
    records = []
    with open(FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] != entry_id:
                records.append(row)
    with open(FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(records)

if __name__ == '__main__':
    setup_file()
    add_entry({'id': '1', 'customer_name': 'Raj Malhotra', 'product': 'TV', 'quantity': '1', 'price': '55000'})
    add_entry({'id': '2', 'customer_name': 'Tina Kapoor', 'product': 'Air Conditioner', 'quantity': '1', 'price': '40000'})
    add_entry({'id': '3', 'customer_name': 'Amit Patel', 'product': 'Refrigerator', 'quantity': '2', 'price': '32000'})
    add_entry({'id': '4', 'customer_name': 'Sonali Jain', 'product': 'Microwave', 'quantity': '1', 'price': '15000'})
    add_entry({'id': '5', 'customer_name': 'Mohit Sinha', 'product': 'Washing Machine', 'quantity': '1', 'price': '30000'})
    
    print("Initial Data:")
    show_entries()
    
    modify_entry('3', {'quantity': '3', 'price': '48000'})
    remove_entry('2')
    
    print("\nFinal Data:")
    show_entries()
