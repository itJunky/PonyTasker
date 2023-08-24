from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class NewTaskForm(FlaskForm):
    title = StringField('Имя задачи', validators=[DataRequired()])
    body = StringField('Описание задачи', validators=[DataRequired()])


class EditTaskForm(FlaskForm):
    title = StringField('Имя задачи', validators=[DataRequired()], render_kw={"placeholder": "t test"})
    body = StringField('Описание задачи', validators=[DataRequired()], render_kw={"placeholder": "b test"})