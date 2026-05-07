from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    min_units: str
    units: str
    tot_enrl: str
    cap_enrl: str
    instructor: str
    capacity: str
    room: str
    mtg_start: str
    mtg_end: str
    days: str
    start_date: str
    end_date: str
    term: str
    campus: str
    class_nbr: str
    total_credits: str
    dup: str
    full: str
    over: str

    @property
    def key(self):
        # Primary key for tree: (subject, catalog, section)
        return (self.subject.strip(), self.catalog.strip(), self.section.strip())