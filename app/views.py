from app import tasker
from .forms import NewTaskForm
from .common import createnewtask, tasklist
from flask import render_template, redirect


@tasker.route('/')
@tasker.route('/index')
def index():
    return "Hello, Worldx!</br><a href=/newtask>Новая задача</a>"


# TODO Список задач
    # TODO помечать задачу выполненной
@tasker.route('/tasklist')
def show_tasks():
    return render_template('tasklist.html', tasklist=tasklist())


# TODO Добавление задачи (сохранение в БД)
@tasker.route('/newtask', methods=['GET', 'POST'])
def create_new_task():
    form = NewTaskForm()
    if form.validate_on_submit():
        print(form.title.data)
        print(form.body.data)
        createnewtask(form.title.data, form.body.data)
        return redirect('/tasklist')
    return render_template('newtask.html', form=form)

# TODO Отображение самой задачи
# TODO Редактирование задачи
