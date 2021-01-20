from echis_web.extensions import me


class User(me.Document):
    discord_id = me.IntField(required=True)
    username = me.StringField(reqired=True)
    avatar = me.URLField(required=True)
    permissions = me.ListField()
