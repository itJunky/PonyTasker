from app import tasker
from .forms import NewTaskForm, EditTaskForm
from .models import Task
from .common import createnewtask, tasklist, edittask
from flask import render_template, redirect, request
from pony.orm import select


@tasker.route('/')
@tasker.route('/index')
def index():
    return "Hello, it's a PonyTasker!</br>" \
           "<a href=/tasklist>Список задач</a></br>" \
           "<a href=/newtask>Новая задача</a>"


# Список задач
    # TODO помечать задачу выполненной
@tasker.route('/tasklist')
def show_tasks():
    sort = request.args.get('sort')
    return render_template('tasklist.html', tasklist=tasklist(sort))


# Добавление задачи
@tasker.route('/newtask', methods=['GET', 'POST'])
def create_new_task():
    form = NewTaskForm()
    if form.validate_on_submit():
        createnewtask(form.title.data, form.body.data)
        return redirect('/tasklist')
    return render_template('newtask.html', form=form)


# Отображение самой задачи
@tasker.route('/task/<int:task_id>')
def show_task(task_id):
    t = select(t for t in Task if t.id == task_id)
    maxtasks = select(t.id for t in Task).max()
    print(maxtasks)
    if task_id > maxtasks:
        return "Нет такой задачи"
    return render_template('task.html', task=list(t)[0])


# Редактирование задачи
@tasker.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    form = EditTaskForm()
    maxtasks = select(t.id for t in Task).max()
    print(maxtasks)
    if task_id > maxtasks:
        return "Нет такой задачи"
    t = select(t for t in Task if t.id == task_id)
    if form.validate_on_submit():
        # TODO сохранение изменений
        edittask(t[0], form.title.data, form.body.data, form.completion.data)
        return redirect('/tasklist')
    return render_template('edit.html', task=list(t)[0], form=form)
