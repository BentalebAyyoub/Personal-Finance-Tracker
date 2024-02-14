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
    
    def get_summary(self, start_date, end_date):
        total_income = 0
        total_expense = 0

        with open(self.csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                date = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                if start_date <= date <= end_date:
                    amount = float(row[0])
                    if amount > 0:
                        total_income += amount
                    else:
                        total_expense += amount

        savings = total_income + total_expense
        return total_income, total_expense, savings

    def display_summary(self):
        print("Enter the start date (YYYY-MM-DD):")
        start_date = datetime.strptime(input(), '%Y-%m-%d')
        print("Enter the end date (YYYY-MM-DD):")
        end_date = datetime.strptime(input(), '%Y-%m-%d')

        total_income, total_expense, savings = self.get_summary(start_date, end_date)

        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Savings: ${savings:.2f}")



# transaction_manager = TransactionManager()

# amount = float(input("Enter transaction amount: "))
# description = input("Enter transaction description: ")

# transaction_manager.display_categories()
# category = transaction_manager.get_category_choice()

# transaction_manager.record_transaction(amount, description, category)
        
# transaction_manager.display_summary()
