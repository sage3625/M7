import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.schedule_dict = {}

    def add_entry(self, item: ScheduleItem):
        key = item.get_key()
        self.schedule_dict[key] = item

    def print_header(self):
        print(f"{'Subject':<6} {'Catalog':<7} {'Section':<8} {'Component':<10} "
              f"{'Session':<8} {'Units':<5} {'TotEnrl':<8} {'CapEnrl':<8} Instructor")
        print("#" * 90)

    def print(self):
        self.print_header()
        for item in self.schedule_dict.values():
            item.print()

    def find_by_subject(self, subject):
        return [item for item in self.schedule_dict.values()
                if item.subject.upper() == subject.upper()]

    def find_by_subject_catalog(self, subject, catalog):
        return [item for item in self.schedule_dict.values()
                if item.subject.upper() == subject.upper()
                and item.catalog.upper() == catalog.upper()]

    def find_by_instructor_last_name(self, last_name):
        return [item for item in self.schedule_dict.values()
                if last_name.lower() in item.instructor.lower()]


def load_csv(filename):
    schedule = Schedule()

    with open(filename, encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            item = ScheduleItem(
                subject=row["Subject"],
                catalog=row["Catalog"],
                section=row["Section"],
                component=row["Component"],
                session=row["Session"],
                units=int(row["Units"]),
                tot_enrl=int(row["TotEnrl"]),
                cap_enrl=int(row["CapEnrl"]),
                instructor=row["Instructor"]
            )
            schedule.add_entry(item)

    return schedule
