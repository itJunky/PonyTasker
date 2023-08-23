from pony.orm import *
from app.settings import settings

db = Database(**settings['sqlite'])


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    completion = Optional(bool)
    title = Optional(str)
    body = Optional(str)


set_sql_debug(True)
db.generate_mapping(create_tables=True)
