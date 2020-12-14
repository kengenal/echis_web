from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL


class AuthForm(FlaskForm):
    discord_id = IntegerField("discord_id", validators=[DataRequired()])
    username = StringField("name", validators=[DataRequired()])
    avatar = StringField("avatar", validators=[URL()])
    permissions = StringField("permissions", validators=[DataRequired()])

    class Meta:
        csrf = False
