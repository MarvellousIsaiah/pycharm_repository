class Entry:

    def __init__(self, id: int, title: str, body: str):
        self.id = id
        self.title = title
        self.body = body
        self.date = 0

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, new_title: str):
        self.title = new_title

    def set_body(self, new_body: str):
        self.body = new_body

    def get_body(self):
        return self.body

    def __repr__(self):
        return self.body + self.title
