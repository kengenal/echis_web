import uuid
from datetime import datetime

import factory

from echis_web.model.share_model import Playlists
from factory import Faker, LazyFunction, lazy_attribute


class PlaylistsFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Playlists

    record_id = str(uuid.uuid4())
    playlist_id = str(uuid.uuid4())
    user = Faker("name")
    api = Faker("name")
    is_active = True
