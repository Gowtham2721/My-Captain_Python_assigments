#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
import os
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook

# File to store expense data
DATA_FILE = "expenses.json"
EXCEL_FILE = "expenses.xlsx"

"""
expenses.json file sholud contain

{
    "categories": [],
    "entries": []
}

Sample Entries for a sample output
{
    "categories": ["groceries", "transportation", "entertainment"],
    "entries": [
        {"amount": 50.25, "description": "Groceries for the week", "category": "groceries"},
        {"amount": 20.50, "description": "Dinner with friends", "category": "entertainment"},
        {"amount": 15.75, "description": "Bus fare", "category": "transportation"},
        {"amount": 35.00, "description": "Movie tickets", "category": "entertainment"}
    ]
}

"""

# Load existing expense data from file if available
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        expenses = json.load(file)
else:
    expenses = {"categories": [], "entries": []}
    
# Function to display menu and get user choice
def display_menu():
    print("\nExpense Recording System Menu:")
    print("1. Add \t\tExpense")
    print("2. Remove \tExpense")
    print("3. View \tExpenses\n")
    print("4. Add \t\tExpense Category")
    print("5. Remove \tExpense Caterogy")
    print("6. View \tExpense Categories\n")
    print("7. Higest Expense")
    print("8. Lowest Expense\n")
    print("9. View \tExpense Summary")
    print("10. Export to Excel\n")
    print("11. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to add a new expense entry
def add_expense():
    try:
        amount = float(input("Enter the amount spent: ₹"))
        description = input("Enter a brief description: ")
        print("Available Categories: " + ", ".join(expenses["categories"]))
        category = input("Enter expense category: ")

        # Add new category if it doesn't exist
        if category not in expenses["categories"]:
            expenses["categories"].append(category)

        entry = {"amount": amount, "description": description, "category": category}
        expenses["entries"].append(entry)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Amount must be numeric.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Function to view all expense entries
def view_expenses():
    if not expenses["entries"]:
        print("No expenses recorded yet.")
    else:
        for index, entry in enumerate(expenses["entries"], start=1):
            print(f"{index}. Amount: ₹{entry['amount']}, Description: {entry['description']}, Category: {entry['category']}")

# Function to view expense categories
def view_categories():
    print("Expense Categories: " + ", ".join(expenses["categories"]))
    
# Function to add a new expense category
def add_category():
    new_category = input("Enter new expense category: ")
    expenses["categories"].append(new_category)
    print(f"Category '{new_category}' added successfully!")
    
# Function to view expense summary
def view_summary():
    if not expenses["entries"]:
        print("No expenses recorded yet.")
    else:
        total_spent = sum(entry["amount"] for entry in expenses["entries"])
        print(f"Total amount spent: ₹{total_spent:.2f}")

        # Display breakdown by categories
        category_expenses = {category: 0 for category in expenses["categories"]}
        for entry in expenses["entries"]:
            category_expenses[entry["category"]] += entry["amount"]

        # Plotting the data
        plt.figure(figsize=(8, 6))
        plt.pie(category_expenses.values(), labels=category_expenses.keys(), autopct='%1.1f%%', startangle=140)
        plt.title("Expense Breakdown by Categories")
        plt.show()
        
# Function to remove an expense category
def remove_category():
    print("Available Categories: " + ", ".join(expenses["categories"]))
    category_to_remove = input("Enter the category to remove: ")

    if category_to_remove in expenses["categories"]:
        expenses["categories"].remove(category_to_remove)
        print(f"Category '{category_to_remove}' removed successfully!")
    else:
        print(f"Category '{category_to_remove}' not found.")

# Function to remove an expense entry
def remove_expense():
    view_expenses()
    try:
        entry_index = int(input("Enter the number of the expense to remove: ")) - 1
        if 0 <= entry_index < len(expenses["entries"]):
            removed_entry = expenses["entries"].pop(entry_index)
            print(f"Expense '{removed_entry['description']}' removed successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a valid expense number.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Function to export expenses to Excel
def export_to_excel():
    
    if not os.path.exists(DATA_FILE):
        print("No expenses recorded yet.")
    else:
        with open(DATA_FILE, "r") as file:
            expenses = json.load(file)
            expense_entries = expenses["entries"]
            
            # Create a DataFrame from the expense entries
            df = pd.DataFrame(expense_entries, columns=["amount", "description", "category"])
            
            # Export DataFrame to Excel file with specified columns
            excel_filename = "expenses.xlsx"
            df.to_excel(excel_filename, index=False, engine='openpyxl')
            
            
            print(f"Expense data exported to '{excel_filename}' successfully.")
    
# Function to find and display the highest expense
def highest_expense():
    if not expenses["entries"]:
        print("No expenses recorded yet.")
        return

    highest_expense_entry = max(expenses["entries"], key=lambda x: x["amount"])
    print(f"Highest Expense: Amount: ₹{highest_expense_entry['amount']}, Description: {highest_expense_entry['description']}, Category: {highest_expense_entry['category']}")

# Function to find and display the lowest expense
def lowest_expense():
    if not expenses["entries"]:
        print("No expenses recorded yet.")
        return

    lowest_expense_entry = min(expenses["entries"], key=lambda x: x["amount"])
    print(f"Lowest Expense: Amount: ₹{lowest_expense_entry['amount']}, Description: {lowest_expense_entry['description']}, Category: {lowest_expense_entry['category']}")

# Main program loop
while True:
    choice = display_menu()

    if choice == "1":
        add_expense()
    elif choice == "2":
        remove_expense()
    elif choice == "3":
        view_expenses()
    elif choice == "4":
        add_category()
    elif choice == "5":
        remove_category()
    elif choice == "6":
        view_categories()
    elif choice == "7":
        highest_expense()
    elif choice == "8":
        lowest_expense()
    elif choice == "9":
        view_summary()    
    elif choice == "10":
        export_to_excel()
    elif choice == "11":
        # Save expenses data to file before exiting
        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file)
        print("Expense data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




