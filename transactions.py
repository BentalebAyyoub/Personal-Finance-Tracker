import os
import csv
from datetime import datetime

class TransactionManager:
    def __init__(self, csv_file='transactions.csv'):
        self.csv_file = csv_file
        self.categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Others']
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

    def display_categories(self):
        print("Select a category:")
        for i, category in enumerate(self.categories, start=1):
            print(f"{i}. {category}")

    def get_category_choice(self):
        while True:
            try:
                choice = int(input("Enter the category number: "))
                if 1 <= choice <= len(self.categories):
                    return self.categories[choice - 1]
                else:
                    print("Invalid category number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")



# transaction_manager = TransactionManager()

# amount = float(input("Enter transaction amount: "))
# description = input("Enter transaction description: ")

# transaction_manager.display_categories()
# category = transaction_manager.get_category_choice()

# transaction_manager.record_transaction(amount, description, category)



