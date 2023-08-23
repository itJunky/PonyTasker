from app import tasker

@tasker.route('/')
@tasker.route('/index')
def index():
    return "Hello, Worldx!"


# TODO Список задач
    # TODO помечать задачу выполненной

# TODO Добавление задачи

# TODO Редактирование задачи
