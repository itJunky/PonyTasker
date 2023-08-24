from pony.orm import select
from .models import Task


def createnewtask(title, body):
    new_task = Task(title=title,
                    body=body,
                    completion=False)
    return print('ok')


def tasklist():
    return list(select(t for t in Task))


def edittask(task, title, body):
    task.title = title
    task.body = body
    return print('ok')
