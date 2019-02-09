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
        with open('./test/example_data_filled.json') as f:
            data = json.load(f)

        response = app.post_json('/start', data)
        assert response.status == '200 OK'

    def test_move(self, app):
        with open('./test/example_data_filled.json') as f:
            data = json.load(f)

        response = app.post_json('/move', data)
        assert response.status == '200 OK'

    def test_end(self, app):
        with open('./test/example_data_filled.json') as f:
            data = json.load(f)

        response = app.post_json('/end', data)
        assert response.status == '200 OK'

