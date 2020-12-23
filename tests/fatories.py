import random
import uuid

import factory
from factory import Faker

from echis_web.model.share_model import Playlists, SharedSongs


class PlaylistsFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Playlists

    record_id = factory.Sequence(lambda n: uuid.uuid4())
    playlist_id = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = Faker("name")
    api = "deezer"
    is_active = True


class SongsFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = SharedSongs

    record_id = factory.Sequence(lambda n: uuid.uuid4())
    playlist_id = factory.Sequence(lambda n: str(uuid.uuid4()))
    added_by = Faker("name")
    rank = random.randint(0, 100)
    song_id = str(uuid.uuid4())
    artist = Faker("name")
    album = Faker("name")
    added_to_playlist = str(uuid.uuid4())
    api = "deezer"
    is_shared = False
    cover = str(uuid.uuid4())
    title = Faker("name")
