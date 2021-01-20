import random
import uuid

import factory
from factory import Faker

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

    discord_id = random.randint(0, 100)
    username = Faker("name")
    avatar = "https://cdn.discordapp.com/widget-avatars" \
             "/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH" \
             "-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA "

    permissions = ["ADMIN"]
