from my_entry import Entry


class Diary:

    def __init__(self, username: str, password: str):
        self.name = username
        self.password = password
        self.is_lock = False
        self.entry_no = 1
        self.entries = list()

    def lock_diary(self):
        self.is_lock = True

    def is_locked(self) -> bool:
        return self.is_lock

    def unlock(self, pin: str):
        if pin == self.password:
            self.is_lock = False

    def create_entry(self, title: str, body: str) -> Entry:
        entry = Entry(self.entry_no, title, body)
        self.entries.append(entry)
        self.entry_no += 1
        return entry

    def find_entry(self, i_d: int) -> Entry:
        for entry in self.entries:
            if entry.get_id() == i_d:
                return entry

    def delete_entry(self, i_d: int):
        found_entry = self.find_entry(i_d)
        self.entries.remove(found_entry)

    def update_entry(self, i_d: int, new_title: str, new_body: str):
        found_entry = self.find_entry(i_d)
        found_entry.set_title(new_title)
        found_entry.set_body(new_body)

    def get_number_of_entry(self):
        return len(self.entries)

    def __repr__(self):
        return self.entry_no
