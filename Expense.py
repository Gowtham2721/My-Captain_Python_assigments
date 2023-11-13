#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json
import os
import matplotlib.pyplot as plt

# File to store expense data
DATA_FILE = "expenses.json"

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
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expense Categories")
    print("4. Add Expense Category")
    print("5. View Expense Summary")
    print("6. Remove a Caterogy")
    print("7. Remove an Expense")
    print("8. Exit")
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

# Main program loop
while True:
    choice = display_menu()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_categories()
    elif choice == "4":
        add_category()
    elif choice == "5":
        view_summary()
    elif choice == "6":
        remove_category()
    elif choice == "7":
        remove_expense()
    elif choice == "8":
        # Save expenses data to file before exiting
        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file)
        print("Expense data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




