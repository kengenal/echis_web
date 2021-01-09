import uuid
from datetime import datetime

from echis_web.extensions import me

SHARE_APIS = [("deezer", "deezer"), ("spotify", "spotify"), ("youtube", "youtube")]


class SharedSongs(me.Document):
    record_id = me.UUIDField(default=uuid.uuid4(), required=False)
    title = me.StringField(required=False)
    rank = me.IntField(required=True)
    song_id = me.StringField(required=True)
    artist = me.StringField(required=False)
    cover = me.StringField(required=False)
    album = me.StringField(required=True)
    playlist_id = me.StringField(required=False)
    added_to_playlist = me.StringField(required=True)
    added_by = me.StringField(required=False)
    created_at = me.DateTimeField(default=datetime.utcnow)
    api = me.StringField(required=False)
    is_shared = me.BooleanField(default=False)


class Playlists(me.Document):
    record_id = me.UUIDField(default=uuid.uuid4())
    playlist_id = me.StringField(required=True, max_length=50, unique=True)
    user = me.StringField()
    api = me.StringField(required=True, choices=SHARE_APIS)
    is_active = me.BooleanField(default=True)
    created_at = me.DateTimeField(default=datetime.utcnow)
