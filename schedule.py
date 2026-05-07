import csv
from schedule_item import ScheduleItem
from search_trees import BSTMap, AVLTreeMap

class Schedule:
    """
    Course schedule that can use either BSTMap or AVLTreeMap as backend.
    """

    def __init__(self, backend="bst"):
        if backend == "avl":
            self._tree = AVLTreeMap()
        else:
            self._tree = BSTMap()

    def load_from_csv(self, filename):
        """
        Load all records from CSV into the tree.
        Assumes UTF-8-sig and DictReader as required.
        """
        with open(filename, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = ScheduleItem(
                    subject=row.get("Subject", ""),
                    catalog=row.get("Catalog", ""),
                    section=row.get("Section", ""),
                    component=row.get("Component", ""),
                    session=row.get("Session", ""),
                    min_units=row.get("MinUnits", ""),
                    units=row.get("Units", ""),
                    tot_enrl=row.get("TotEnrl", ""),
                    cap_enrl=row.get("CapEnrl", ""),
                    instructor=row.get("Instructor", ""),
                    capacity=row.get("Capacity", ""),
                    room=row.get("Room", ""),
                    mtg_start=row.get("Mtg Start", ""),
                    mtg_end=row.get("Mtg End", ""),
                    days=row.get("Days", ""),
                    start_date=row.get("Start Date", ""),
                    end_date=row.get("End Date", ""),
                    term=row.get("Term", ""),
                    campus=row.get("Campus", ""),
                    class_nbr=row.get("Class Nbr", ""),
                    total_credits=row.get("Total Credits", ""),
                    dup=row.get("DUP", ""),
                    full=row.get("FULL", ""),
                    over=row.get("OVER", "")
                )
                self._tree.insert(item.key, item)

    def record_count(self):
        return sum(1 for _ in self._tree.inorder_items())

    def inorder_items(self):
        for _, item in self._tree.inorder_items():
            yield item

    def height(self):
        return self._tree.height()

    # ------------------- SEARCH HELPERS -------------------

    def search_by_subject(self, subject):
        subject = subject.strip()
        results = []
        for _, item in self._tree.inorder_items():
            if item.subject.strip() == subject:
                results.append(item)
        return results

    def search_by_subject_catalog(self, subject, catalog):
        subject = subject.strip()
        catalog = catalog.strip()
        results = []
        for _, item in self._tree.inorder_items():
            if item.subject.strip() == subject and item.catalog.strip() == catalog:
                results.append(item)
        return results

    def search_by_instructor(self, instructor_substr):
        instructor_substr = instructor_substr.lower().strip()
        results = []
        for _, item in self._tree.inorder_items():
            if instructor_substr in item.instructor.lower():
                results.append(item)
        return results
