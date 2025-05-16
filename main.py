from src.authentication.admin_login import login_admin
from src.authentication.customer_login import login_customer
from src.authentication.staff_login import login_staff

def main_menu():
    while True:
        print("\n=== Welcome to Restaurant Management System ===")
        print("1. Admin login")
        print("2. Customer login")
        print("3. Staff login")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            login_admin()
        elif choice == '2':
            login_customer()
        elif choice == '3':
            login_staff()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()