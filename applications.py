from file_manager import save_data, read_data


def apply_for_job():
    print("\n=== APPLY FOR A JOB ===")

    users = read_data("data/users.txt")
    jobs = read_data("data/jobs.txt")

    if len(users) == 0:
        print("No registered users found.")
        print("Please register a user first.")
        return

    if len(jobs) == 0:
        print("No jobs are available.")
        print("Please add a job first.")
        return

    email = input("Enter your registered email: ")

    user_found = False

    for user in users:
        user = user.strip()
        details = user.split(",")

        if email == details[1]:
            user_found = True
            user_name = details[0]

    if user_found == False:
        print("User not found.")
        print("Please register with this email first.")
        return

    print("\nAvailable Jobs:")

    number = 1

    for job in jobs:
        job = job.strip()
        details = job.split(",")

        print("\n", number, ".", details[0])
        print("Company :", details[1])
        print("Location:", details[2])
        print("Type    :", details[3])

        number = number + 1

    choice = input("\nEnter the job number you want to apply for: ")

    if choice.isdigit():
        job_number = int(choice)

        if 1 <= job_number <= len(jobs):
            selected_job = jobs[job_number - 1].strip()
            job_details = selected_job.split(",")

            application = (
                user_name + "," +
                email + "," +
                job_details[0] + "," +
                job_details[1]
            )

            save_data("data/applications.txt", application)

            print("\nApplication submitted successfully!")
            print("Applicant :", user_name)
            print("Job       :", job_details[0])
            print("Company   :", job_details[1])
        else:
            print("Invalid job number.")
    else:
        print("Please enter a number.")

    print("===")


def view_applications():
    print("\n=== JOB APPLICATIONS ===")

    applications = read_data("data/applications.txt")

    if len(applications) == 0:
        print("No applications have been submitted yet.")
    else:
        number = 1

        for application in applications:
            application = application.strip()
            details = application.split(",")

            print("\nApplication", number)
            print("Applicant :", details[0])
            print("Email     :", details[1])
            print("Job       :", details[2])
            print("Company   :", details[3])

            number = number + 1

    print("===")