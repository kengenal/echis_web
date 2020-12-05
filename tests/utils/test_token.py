import pytest
from flask import current_app

from echis_web.utils.token import create_token, decode_token


class TestCreateToken:
    def test_create_token_correct_data(self):
        token = create_token({"test": "test"}, options={"TOKEN_SECRET": "OSIEM", "TOKEN_ALGORITHM": "HS256"})

        assert isinstance(token, str)


class TestDecodeToken:
    def test_decode_token_invalid_token_should_be_raise_type_exception(self):
        with pytest.raises(Exception) as error:
            token = create_token({"test": "test"}, options={"TOKEN_SECRET": "OSIEM", "TOKEN_ALGORITHM": "HS256"})
            _ = decode_token(token + "asdasdsad")

            assert error.value == "TypeError: can't concat str to bytes"

    def test_decode_token_with_correct_data(self):
        options = {"TOKEN_SECRET": "OSIEM", "TOKEN_ALGORITHM": "HS256"}
        token = create_token({"test": "test"}, options=options)
        decode = decode_token(token, options=options)

        assert "test" in decode
