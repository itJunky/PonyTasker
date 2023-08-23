from app import tasker
from .forms import NewTaskForm
from flask import render_template, redirect

@tasker.route('/')
@tasker.route('/index')
def index():
    return "Hello, Worldx!</br><a href=/newtask>Новая задача</a>"


# TODO Список задач
    # TODO помечать задачу выполненной

# TODO Добавление задачи (форма ввода)
@tasker.route('/newtask', methods=['GET', 'POST'])
def create_new_task():
    form = NewTaskForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('newtask.html', form=form)

# TODO Отображение самой задачи
# TODO Редактирование задачи
