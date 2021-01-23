import uuid

from echis_web.exception.exceptions import UnauthorizedException
from echis_web.extensions import me


class User(me.Document):
    public_id = me.UUIDField(default=uuid.uuid4())
    discord_id = me.IntField(required=True)
    username = me.StringField(reqired=True)
    avatar = me.URLField(required=True)
    permissions = me.ListField()

    @staticmethod
    def get_user_or_rise_exception(public_id):
        if user := User.objects(public_id=public_id):
            return user
        raise UnauthorizedException()
