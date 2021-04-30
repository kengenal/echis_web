from echis_web.controllers.api.api_auth_controller import ApiAuthController, ApiLogoutController
from echis_web.controllers.api.api_share_controller import ApiPlaylistController, ApiSongController
from echis_web.controllers.api.api_weather_controller import ApiWeatherController
from echis_web.controllers.api.api_filter_controller import ApiFilterController


def route(app):
    """ flask routes """
    # AUTH
    app.add_url_rule("/api/auth", view_func=ApiAuthController.as_view("api_auth"))
    app.add_url_rule("/api/logout", view_func=ApiLogoutController.as_view("api_logout"))

    # PLAYLIST
    app.add_url_rule(
        "/api/share/playlist",
        view_func=ApiPlaylistController.as_view("share_playlist"),
        methods=["GET", "POST"]
    )
    app.add_url_rule(
        "/api/share/playlist/<int:page>",
        view_func=ApiPlaylistController.as_view("share_playlist_pag"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/playlist/<string:playlist_id>",
        view_func=ApiPlaylistController.as_view("share_playlist_parameter"),
        methods=["PUT", "DELETE"]
    )

    # SONGS
    app.add_url_rule(
        "/api/share/songs",
        view_func=ApiSongController.as_view("share_songs"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/songs/<int:page>",
        view_func=ApiSongController.as_view("share_songs_pagination"),
        methods=["GET"]
    )
    app.add_url_rule(
        "/api/share/songs/<string:record_id>",
        view_func=ApiSongController.as_view("share_songs_parameter"),
        methods=["DELETE"]
    )

    # FILTERApiPlaylistController
    app.add_url_rule("/api/filter/words", view_func=ApiFilterController.as_view("filter_module"),
                     methods=["GET", "POST"])
    app.add_url_rule("/api/filter/words/<string:word_id>",
                     view_func=ApiFilterController.as_view("filter_module_remove"),
                     methods=["DELETE"])

    # weather
    app.add_url_rule("/api/weather", view_func=ApiWeatherController.as_view("weather"),
                     methods=["GET"])

    app.add_url_rule("/api/weather/<string:city>",
                     view_func=ApiWeatherController.as_view("weather_with_city"),
                     methods=["GET"])
