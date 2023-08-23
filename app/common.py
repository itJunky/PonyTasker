from pony.orm import db_session, select
from .models import db, Task


# @db_session
def createnewtask(title, body):
    new_task = Task(title=title,
                    body=body,
                    completion=False)
    # db.commit()
    return print('ok')


# @db_session
def tasklist():
    return list(select(t for t in Task))
