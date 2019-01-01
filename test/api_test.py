import pytest
import json
from webtest import TestApp # type: ignore
from app import main

class TestApi:
    @pytest.fixture
    def app(self):
        return TestApp(main.app)

    def test_ping(self, app):
        response = app.post('/ping')
        assert response.status == '200 OK'

    def test_start(self, app):
        json = {
            'game': {
                'id': '1234abcd'
            }
        }
        response = app.post_json('/start', json)
        assert response.status == '200 OK'

    def test_move(self, app):
        json = {
            'game': {
                'id': '1234abcd'
            }
        }
        response = app.post_json('/move', json)
        assert response.status == '200 OK'

    def test_end(self, app):
        json = {
            'game': {
                'id': '1234abcd'
            }
        }
        response = app.post_json('/end', json)
        assert response.status == '200 OK'

