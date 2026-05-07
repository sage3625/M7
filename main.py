from schedule import Schedule

CSV_FILE = "courses_2023.csv"

def print_item(item):
    print(f"{item.subject} {item.catalog}-{item.section} "
          f"{item.days} {item.mtg_start}-{item.mtg_end} "
          f"{item.instructor} (Room {item.room})")

def run_menu(schedule, label):
    while True:
        print(f"\n--- Course Schedule ({label}) ---")
        print("1. List all courses (inorder)")
        print("2. Search by subject")
        print("3. Search by subject + catalog")
        print("4. Search by instructor")
        print("5. Display tree height")
        print("0. Quit this backend")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            for item in schedule.inorder_items():
                print_item(item)
            print(f"\nTotal records: {schedule.record_count()}")

        elif choice == "2":
            subj = input("Subject (e.g., CSC): ")
            results = schedule.search_by_subject(subj)
            print(f"Found {len(results)} result(s):")
            for item in results:
                print_item(item)

        elif choice == "3":
            subj = input("Subject (e.g., CSC): ")
            cat = input("Catalog (e.g., 222): ")
            results = schedule.search_by_subject_catalog(subj, cat)
            print(f"Found {len(results)} result(s):")
            for item in results:
                print_item(item)

        elif choice == "4":
            instr = input("Instructor substring (e.g., 'Schaffner'): ")
            results = schedule.search_by_instructor(instr)
            print(f"Found {len(results)} result(s):")
            for item in results:
                print_item(item)

        elif choice == "5":
            h = schedule.height()
            print(f"Tree height (edges on longest path): {h}")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def main():
    # Load BST version
    bst_schedule = Schedule(backend="bst")
    print("Loading BST schedule...")
    bst_schedule.load_from_csv(CSV_FILE)
    print(f"BST loaded with {bst_schedule.record_count()} records.")
    run_menu(bst_schedule, "BST")

    # Load AVL version
    avl_schedule = Schedule(backend="avl")
    print("Loading AVL schedule...")
    avl_schedule.load_from_csv(CSV_FILE)
    print(f"AVL loaded with {avl_schedule.record_count()} records.")
    run_menu(avl_schedule, "AVL")

if __name__ == "__main__":
    main()