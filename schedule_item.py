from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self):
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        print(f"{self.subject:<6} {self.catalog:<7} {self.section:<8} "
              f"{self.component:<10} {self.session:<8} {self.units:<5} "
              f"{self.tot_enrl:<8} {self.cap_enrl:<8} {self.instructor}")
