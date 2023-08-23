from pony.orm import *


db = Database()


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    completion = Optional(bool)
    title = Optional(str)
    body = Optional(str)


db.generate_mapping()
