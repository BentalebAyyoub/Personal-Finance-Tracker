import os
import csv
from datetime import datetime

class TransactionManager:
    def __init__(self, csv_file='transactions.csv'):
        self.csv_file = csv_file
        self.create_csv()

    def create_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Amount', 'Description', 'Category', 'Date'])

    def record_transaction(self, amount, description, category):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, description, category, date])
        print("Transaction recorded successfully.")


# transaction_manager = TransactionManager()

# amount = float(input("Enter transaction amount: "))
# description = input("Enter transaction description: ")
# category = input("Enter transaction category: ")

# transaction_manager.record_transaction(amount, description, category)


