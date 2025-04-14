class Task:
    def __init__(self, title, status="To Do"):
        self.title = title
        self.status = status

    def mark_done(self):
        self.status = "done"
        