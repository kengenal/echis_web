#! ../env/bin/python
# -*- coding: utf-8 -*-
from echis_web import create_app


class TestConfig:
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app("dev")

        assert app.config['DEBUG'] is True
        assert "MONGODB_SETTINGS" in app.config.keys()

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app("test")

        assert app.config['DEBUG'] is True

    def test_prod_config(self):
        """ Tests if the production config loads correctly """

        app = create_app("prod")

        assert "MONGODB_SETTINGS" in app.config.keys()
