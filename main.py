from schedule import load_csv

def print_results(results, schedule):
    if not results:
        print("No matching courses found.\n")
        return

    schedule.print_header()
    for item in results:
        item.print()
    print()

def main():
    filename = "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"
    schedule = load_csv(filename)

    while True:
        print("\n--- Course Schedule System ---")
        print("1. Display full schedule")
        print("2. Search by subject")
        print("3. Search by subject + catalog")
        print("4. Search by instructor last name")
        print("5. Quit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter subject (e.g., BIO): ").strip()
            results = schedule.find_by_subject(subject)
            print_results(results, schedule)

        elif choice == "3":
            subject = input("Enter subject (e.g., BIO): ").strip()
            catalog = input("Enter catalog number (e.g., 141): ").strip()
            results = schedule.find_by_subject_catalog(subject, catalog)
            print_results(results, schedule)

        elif choice == "4":
            last_name = input("Enter instructor last name: ").strip()
            results = schedule.find_by_instructor_last_name(last_name)
            print_results(results, schedule)

        elif choice == "5":
            print("Ending program.")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
