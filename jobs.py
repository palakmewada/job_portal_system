from file_manager import save_data, read_data


job_types = ("Full-Time", "Part-Time", "Internship")


def add_job():
    print("\n=== ADD NEW JOB ===")

    title = input("Enter job title: ")
    company = input("Enter company name: ")
    location = input("Enter job location: ")

    print("\nSelect Job Type:")
    print("1. Full-Time")
    print("2. Part-Time")
    print("3. Internship")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        job_type = job_types[0]
    elif choice == "2":
        job_type = job_types[1]
    elif choice == "3":
        job_type = job_types[2]
    else:
        print("Invalid job type.")
        return

    skills = input("Enter required skills: ")

    job = {
        "title": title,
        "company": company,
        "location": location,
        "type": job_type,
        "skills": skills
    }

    data = (
        job["title"] + "," +
        job["company"] + "," +
        job["location"] + "," +
        job["type"] + "," +
        job["skills"]
    )

    save_data("data/jobs.txt", data)

    print("\nJob added successfully!")
    print("Job Title :", job["title"])
    print("Company   :", job["company"])
    print("Location  :", job["location"])
    print("Job Type  :", job["type"])
    print("Skills    :", job["skills"])
    print("===")


def view_jobs():
    print("\n=== AVAILABLE JOBS ===")

    jobs = read_data("data/jobs.txt")

    if len(jobs) == 0:
        print("No jobs are available right now.")
    else:
        number = 1

        for job in jobs:
            job = job.strip()
            details = job.split(",")

            print("\nJob", number)
            print("Job Title :", details[0])
            print("Company   :", details[1])
            print("Location  :", details[2])
            print("Job Type  :", details[3])
            print("Skills    :", details[4])

            number = number + 1

    print("===")