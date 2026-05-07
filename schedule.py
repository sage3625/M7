import csv
from schedule_item import ScheduleItem
from search_trees import BSTMap, AVLTreeMap

class Schedule:
    def __init__(self, backend="bst"):
        if backend == "avl":
            self.tree = AVLTreeMap()
        else:
            self.tree = BSTMap()

    def load_from_csv(self, filename):
        with open(filename, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = ScheduleItem(
                    subject=row["Subject"],
                    catalog=row["Catalog"],
                    section=row["Section"],
                    component=row["Component"],
                    session=row["Session"],
                    units=row["Units"],
                    tot_enrl=row["TotEnrl"],
                    cap_enrl=row["CapEnrl"],
                    instructor=row["Instructor"]
                )
                self.tree.insert(item.get_key(), item)

    def print_header(self):
        print(f"{'Subj':<6} {'Cat':<6} {'Sec':<6} {'Comp':<8} "
              f"{'Sess':<6} {'Unit':<4} {'Enrl':<6} {'Cap':<6} Instructor")
        print("-" * 80)

    def print_all(self):
        self.print_header()
        for _, item in self.tree.inorder_items():
            item.print()

    def find_by_subject(self, subject):
        return [item for _, item in self.tree.inorder_items()
                if item.subject.upper() == subject.upper()]

    def find_by_subject_catalog(self, subject, catalog):
        return [item for _, item in self.tree.inorder_items()
                if item.subject.upper() == subject.upper()
                and item.catalog.upper() == catalog.upper()]

    def find_by_instructor(self, last_name):
        return [item for _, item in self.tree.inorder_items()
                if last_name.lower() in item.instructor.lower()]

    def height(self):
        return self.tree.height()

    def record_count(self):
        return sum(1 for _ in self.tree.inorder_items())
