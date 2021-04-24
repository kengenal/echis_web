import random
import uuid
from datetime import datetime

import factory
from factory import Faker

from echis_web.model.filter_model import FilterModel
from echis_web.model.share_model import Playlists, SharedSongs
from echis_web.model.user_model import User


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


class UserFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = User

    public_id = factory.Sequence(lambda n: uuid.uuid4())
    discord_id = random.randint(0, 100)
    username = Faker("name")
    avatar = factory.Sequence(
        lambda n: "https://cdn.discordapp.com/widget-avatars/72hdNk-aQzhCtMttVXuS3jdY2bGCKRIWZ0qcuBwtf0Q" \
                  "/cB7zPbxBXEZH_H0solsOPkwLo27UKXyj5mwQrVfBcTKea" \
                  "-cwgvqwoA5lHC2cQ5ISonuVK7KXjmWYRYjusSp2g4HVqiCWpjhE3Qp0OoXXCN5VnLh7PEjajbpS74Ez428mIX9dPJ6azi37sw")

    permissions = ["ADMIN"]


class FilterFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = FilterModel

    name = Faker("name")
    created_at = factory.Sequence(lambda n: datetime.utcnow)
