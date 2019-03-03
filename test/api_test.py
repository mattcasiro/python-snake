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

        try:
            response = app.post_json('/move', data)
            assert response.status == '200 OK'
        except Exception as err:
            assert 0, err
            print (err)

    def test_move_validates(self, app):
        data = {
            'board': {
                'food': [{'x': 1, 'y': 1}],
                'height': 10,
                'snakes': [{
                    'body': [{'x': 2, 'y': 2}],
                    'health': 0,
                    'id': 'you',
                    'name': 'you'
                }],
                'width': 10
            },
            'game': {'id': '1551571647904662475'},
            'turn': 1,
            'you': {
                'body': [{'x': 2, 'y': 2}],
                'health': 0,
                'id': 'you',
                'name': 'you'
            }
        }
        assert 1

    def test_end(self, app):
        with open('./test/example_data_filled.json') as f:
            data = json.load(f)

        response = app.post_json('/end', data)
        assert response.status == '200 OK'

