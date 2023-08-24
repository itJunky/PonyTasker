from app import tasker
from .forms import NewTaskForm
from .models import Task
from .common import createnewtask, tasklist
from flask import render_template, redirect
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
    return render_template('tasklist.html', tasklist=tasklist())


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
    t = select(t for t in Task if t.id == task_id)[:]
    print(type(t))
    print(t)
    return render_template('task.html', task=t[0])

# TODO Редактирование задачи


