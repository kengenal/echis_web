from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL

from echis_web.models.user_model import User


class AuthForm(FlaskForm):
    discord_id = IntegerField("discord_id", validators=[DataRequired()])
    username = StringField("name", validators=[DataRequired()])
    avatar = StringField("avatar", validators=[URL()])
    permissions = StringField("permissions", validators=[DataRequired()])

    class Meta:
        csrf = False

    def save(self):
        user = User(
            discord_id=self.discord_id,
            username=self.username,
            avatar=self.avatar,
            permissions=self.permissions
        )
        user.save()
        return user.public_id
