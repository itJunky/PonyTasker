from pony.orm import select
from .models import Task


def createnewtask(title, body):
    new_task = Task(title=title,
                    body=body,
                    completion=False)
    return print('ok')


def tasklist(sort):
    lst = list(select(t for t in Task))
    if sort == 'cmplup':
        lst = sortdblsel(lst, 'up')
    elif sort == 'cmpldwn':
        lst = sortdblsel(lst, 'dwn')
    # Todo добавлять другие виды сортировок сюда
    return lst


def edittask(task, title, body, completion):
    task.title = title
    task.body = body
    task.completion = completion
    return print('ok')


def sortdblsel(tlist, stype):
    # TODO зарефакторить на перебор исходного класса
    completed = list()
    uncompleted = list()
    for i, el in enumerate(tlist):
        if el.completion:
            completed.append(el)
        else:
            uncompleted.append(el)

    if stype == 'up':
        return completed + uncompleted
    else:
        return uncompleted + completed
