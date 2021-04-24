from datetime import datetime

from echis_web.extensions import me


class FilterModel(me.Document):
    name = me.StringField(required=True, unique=True)
    created_at = me.DateTimeField(default=datetime.utcnow)
