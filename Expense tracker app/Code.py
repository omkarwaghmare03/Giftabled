from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
@app.get("/expenses/{expense}")
def get_expense(expense: int):
    expenses = load_expenses()

    for item in expenses:
        if item.get("id") == expense:
            return item

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)



def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category (Food/Travel/Shopping): ")
        description = input("Enter description: ")

        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")
        
@app.add("/expenses/{expense}")
def add_expense(expense: int):
    expenses = load_expenses()

    for item in expenses:
        if item.get("id") == expense:
            return item

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']:.2f} | "
            f"Description: {expense['description']}"
        )


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = (
            summary.get(category, 0) + expense["amount"]
        )

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
