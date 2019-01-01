import os
import sys
import random
from bottle import debug, default_app, post, request, route, run
from configparser import ConfigParser

from app import api

config = ConfigParser()
config.read('config.ini')
if 'APP_ENV' not in config['DEFAULT']:
    print('Missing required configurations, server shutting down.')
    sys.exit()

@post('/ping')
def ping():
    return api.ping_response()

@post('/start')
def start():
    data = request.json
    print ("Starting game %s" % data["game"]["id"])
    return api.start_response("#00ff00")


@post('/move')
def move():
    data = request.json

    # TODO: Do things with data

    directions = ['up', 'down', 'left', 'right']
    direction = 'right'#random.choice(directions)

    print ("Moving %s" % direction)
    return api.move_response(direction)


@post('/end')
def end():
    data = request.json
    print ("Game %s ended" % data["game"]["id"])
    return api.end_response()


# Expose WSGI app (so gunicorn can find it)
app = default_app()

if __name__ == '__main__':
    run(app,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        reloader=(config['DEFAULT']['APP_ENV'] != 'production'),
        debug=(config['DEFAULT']['APP_ENV'] != 'production')
    )
