from schedule import Schedule

CSV_FILE = "courses_2023.csv"

def print_results(results, schedule):
    if not results:
        print("No matching courses found.\n")
        return

    schedule.print_header()
    for item in results:
        item.print()
    print()

def run_menu(schedule, label):
    while True:
        print(f"\n--- Course Schedule System ({label}) ---")
        print("1. Display full schedule")
        print("2. Search by subject")
        print("3. Search by subject + catalog")
        print("4. Search by instructor last name")
        print("5. Display tree height")
        print("6. Quit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            schedule.print_all()

        elif choice == "2":
            subject = input("Enter subject: ").strip()
            print_results(schedule.find_by_subject(subject), schedule)

        elif choice == "3":
            subject = input("Enter subject: ").strip()
            catalog = input("Enter catalog: ").strip()
            print_results(schedule.find_by_subject_catalog(subject, catalog), schedule)

        elif choice == "4":
            last = input("Enter instructor last name: ").strip()
            print_results(schedule.find_by_instructor(last), schedule)

        elif choice == "5":
            print(f"Tree height: {schedule.height()}")

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.\n")

def main():
    print("Choose backend:")
    print("1. BST")
    print("2. AVL")
    backend_choice = input("Enter choice: ").strip()

    backend = "bst" if backend_choice == "1" else "avl"

    schedule = Schedule(backend=backend)
    print(f"\nLoading schedule using {backend.upper()} backend...")
    schedule.load_from_csv(CSV_FILE)
    print(f"Loaded {schedule.record_count()} records.")

    run_menu(schedule, backend.upper())

if __name__ == "__main__":
    main()
