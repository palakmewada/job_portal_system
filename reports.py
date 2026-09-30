from file_manager import read_data


def show_reports():
    print("\n=== JOB PORTAL REPORTS ===")

    users = read_data("data/users.txt")
    jobs = read_data("data/jobs.txt")
    applications = read_data("data/applications.txt")

    total_users = len(users)
    total_jobs = len(jobs)
    total_applications = len(applications)

    print("\nTotal Registered Users :", total_users)
    print("Total Jobs Posted     :", total_jobs)
    print("Total Applications    :", total_applications)

    print("\n---")

    if total_users == 0:
        print("No users have registered yet.")
    else:
        print("Users are registered on the portal.")

    if total_jobs == 0:
        print("No jobs have been posted yet.")
    else:
        print("Jobs are available on the portal.")

    if total_applications == 0:
        print("No job applications have been received.")
    else:
        print("Job applications have been received.")

    print("===")