from users import register_user, view_users
from jobs import add_job, view_jobs
from search import search_jobs
from applications import apply_for_job, view_applications
from reports import show_reports


def show_menu():
    print("\n===")
    print("JOB PORTAL SYSTEM")
    print("===")
    print("1. Register User")
    print("2. View Registered Users")
    print("3. Add New Job")
    print("4. View Available Jobs")
    print("5. Search Jobs")
    print("6. Apply for a Job")
    print("7. View Applications")
    print("8. View Job Portal Reports")
    print("9. Exit")
    print("===")


while True:
    show_menu()

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        register_user()

    elif choice == "2":
        view_users()

    elif choice == "3":
        add_job()

    elif choice == "4":
        view_jobs()

    elif choice == "5":
        search_jobs()

    elif choice == "6":
        apply_for_job()

    elif choice == "7":
        view_applications()

    elif choice == "8":
        show_reports()

    elif choice == "9":
        print("\nThank you for using the Job Portal System!")
        print("Program closed successfully.")
        break

    else:
        print("\nInvalid choice!")
        print("Please enter a number from 1 to 9.")