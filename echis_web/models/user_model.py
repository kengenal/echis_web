from uuid import uuid4

from mongoengine import StringField, IntField, URLField, UUIDField

from echis_web import me


class User(me.Document):
    username = StringField(max_length=50, required=True)
    discord_id = IntField(required=True)
    avatar = URLField(required=True)
    permissions = StringField(required=True)
    public_id = UUIDField(default=uuid4())

    def has_perm(self, val):
        perms = self.permissions.split()
        return val in perms
