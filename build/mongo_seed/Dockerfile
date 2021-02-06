FROM mongo:latest

COPY ./build/mongo_seed/data /tmp/mongo


COPY ./build/mongo_seed/entrypoint /entrypoint
RUN chmod 775 /entrypoint

ENTRYPOINT ["sh", "/entrypoint"]
