FROM mongo

COPY ./build/mongo_seed/data /tmp/mongo

CMD mongoimport --host mongo --db admin --collection playlists --type json --file /tmp/mongo/playlist.json --jsonArray
CMD mongoimport --host mongo --db admin --collection shared_songs --type json --file /tmp/mongo/shared_songs.json --jsonArray
