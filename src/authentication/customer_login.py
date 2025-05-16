import uuid
import json
import os
import getpass
def back_to_menu():
    input("\nPress Enter to go back to the menu...")

def load_data(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def is_unique_id(users, user_id):
    return all(user['id'] != user_id for user in users)

def is_unique_email(users, email):
    return all(user['email'] != email for user in users)
def register_customer():
    print("\n=== Customer sing_up ===")
    filename = "customer.json"
    customers = load_data(filename)

    while True:
        user_id = input("Enter Customer ID: ")
        if not is_unique_id(customers, user_id):
            print("ID already exists! Try a different one.")
        else:
            break

    while True:
        email = input("Enter Email: ")
        if not is_unique_email(customers, email):
            print("Email already sing_up! Try another one.")
        else:
            break

    customer = {
        "id": user_id,
        "name": input("Enter Name: "),
        "email": email,
        "password": getpass.getpass("Create Password: "),
        "contact": input("Enter Contact Number: "),
        "address": input("Enter Address: ")
    }

    customers.append(customer)
    save_data(filename, customers)
    print("\nCustomer sing_up Successfully!")
    back_to_menu()

def login_customer():
    print("\n=== Customer Login ===")
    filename = "customer.json"
    customers = load_data(filename)

    email = input("Enter Email: ")
    password = getpass.getpass("Enter Password: ")

    for customer in customers:
        if customer['email'] == email and customer['password'] == password:
            print(f"\nWelcome {customer['name']}! Login Successful.")
            customer_dashboard(customer)
            break
    else:
        print("\nInvalid Email or Password.")
        back_to_menu()
def customer_dashboard(current_customer):
    while True:
        print(f"\n--- Customer Dashboard ---")
        print("1. View My Profile")
        print("2. Change Password")
        print("3. Delete My Account")
        print("4. Logout")

        choice = input("Enter your choice: ")
        filename = "customer.json"
        customers = load_data(filename)

        if choice == '1':
            print("\n--- My Profile ---")
            for key, value in current_customer.items():
                if key != "password":
                    print(f"{key.capitalize()}: {value}")
            back_to_menu()

        elif choice == '2':
            old_pass = getpass.getpass("Enter Current Password: ")
            if old_pass == current_customer['password']:
                new_pass = getpass.getpass("Enter New Password: ")
                confirm_pass = getpass.getpass("Confirm New Password: ")
                if new_pass == confirm_pass:
                    for customer in customers:
                        if customer['id'] == current_customer['id']:
                            customer['password'] = new_pass
                            break
                    save_data(filename, customers)
                    print("Password Changed Successfully.")
                else:
                    print("Passwords didn't match.")
            else:
                print("Incorrect Current Password.")
            back_to_menu()

        elif choice == '3':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                customers = [customer for customer in customers if customer['id'] != current_customer['id']]
                save_data(filename, customers)
                print("Account Deleted Successfully.")
                break
            else:
                print("Account deletion cancelled.")
            back_to_menu()

        elif choice == '4':
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")
            back_to_menu()
def customer_menu():
    while True:
        print("\n--- Customer Management ---")
        print("1. sing_up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_customer()
        elif choice == '2':
            login_customer()
        elif choice == '3':
            print("Exiting Customer Management.")
            break
        else:
            print("Invalid choice.")
            back_to_menu()
if __name__ == "__main__":
    customer_menu()