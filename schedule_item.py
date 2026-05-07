from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: str
    tot_enrl: str
    cap_enrl: str
    instructor: str

    def get_key(self):
        return (self.subject.strip(), self.catalog.strip(), self.section.strip())

    def print(self):
        print(f"{self.subject:<6} {self.catalog:<6} {self.section:<6} "
              f"{self.component:<8} {self.session:<6} "
              f"{self.units:<4} {self.tot_enrl:<6} {self.cap_enrl:<6} "
              f"{self.instructor}")
