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
def register_admin():
    print("\n=== Admin sing_up ===")
    filename = "admin.json"
    admins = load_data(filename)

    while True:
        user_id = input("Enter Admin ID: ")
        if not is_unique_id(admins, user_id):
            print("ID already exists! Try a different one.")
        else:
            break

    while True:
        email = input("Enter Email: ")
        if not is_unique_email(admins, email):
            print("Email already singup! Try another one.")
        else:
            break

    admin = {
        "id": user_id,
        "name": input("Enter Name: "),
        "email": email,
        "password": getpass.getpass("Create Password: "),
        "contact": input("Enter Contact Number: "),
        "address": input("Enter Address: ")
    }

    admins.append(admin)
    save_data(filename, admins)
    print("\nAdmin sing_up Successfully!")
    back_to_menu()

def login_admin():
    print("\n=== Admin Login ===")
    filename = "admin.json"
    admins = load_data(filename)

    email = input("Enter Email: ")
    password = getpass.getpass("Enter Password: ")

    for admin in admins:
        if admin['email'] == email and admin['password'] == password:
            print(f"\nWelcome {admin['name']}! Login Successful.")
            admin_dashboard(admin)
            break
    else:
        print("\nInvalid Email or Password.")
        back_to_menu()
def admin_dashboard(current_admin):
    while True:
        print(f"\n--- Admin Dashboard ---")
        print("1. View My Profile")
        print("2. Change Password")
        print("3. Delete My Account")
        print("4. Logout")

        choice = input("Enter your choice: ")
        filename = "admin.json"
        admins = load_data(filename)

        if choice == '1':
            print("\n--- My Profile ---")
            for key, value in current_admin.items():
                if key != "password":
                    print(f"{key.capitalize()}: {value}")
            back_to_menu()

        elif choice == '2':
            old_pass = getpass.getpass("Enter Current Password: ")
            if old_pass == current_admin['password']:
                new_pass = getpass.getpass("Enter New Password: ")
                confirm_pass = getpass.getpass("Confirm New Password: ")
                if new_pass == confirm_pass:
                    for admin in admins:
                        if admin['id'] == current_admin['id']:
                            admin['password'] = new_pass
                            break
                    save_data(filename, admins)
                    print("Password Changed Successfully.")
                else:
                    print("Passwords didn't match.")
            else:
                print("Incorrect Current Password.")
            back_to_menu()

        elif choice == '3':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                admins = [admin for admin in admins if admin['id'] != current_admin['id']]
                save_data(filename, admins)
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
def admin_menu():
    while True:
        print("\n--- Admin Management ---")
        print("1. sing_up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_admin()
        elif choice == '2':
            login_admin()
        elif choice == '3':
            print("Exiting Admin Management.")
            break
        else:
            print("Invalid choice.")
            back_to_menu()
if __name__ == "__main__":
    admin_menu()