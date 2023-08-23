from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class NewTaskForm(FlaskForm):
    title = StringField('Имя задачи', validators=[DataRequired()])
    body = StringField('Описание задачи', validators=[DataRequired()])
