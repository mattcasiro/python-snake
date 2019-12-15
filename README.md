# Python-Snake

![python version](https://img.shields.io/badge/Python-3.7.7-brightgreen.svg)

A [Battlesnake AI](http://battlesnake.io) written in Python 3, based off the [python-starter-snake](https://github.com/battlesnakeio/starter-snake-python).

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

#### You will need...

* a working Python 3.7 development environment ([getting started guide](http://hackercodex.com/guide/python-development-environment-on-mac-osx/))
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

## Running the Snake Locally

1) [Fork this repo](https://github.com/sendwithus/battlesnake-python/fork).

2) Clone repo to your development environment:
```
git clone git@github.com:username/battlesnake-python.git
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run unit tests
```
pip install -r requirements.dev.txt
pytest
```

5) Run local server:
```
python app/main.py
```

5) Test client in your browser: [http://localhost:8080](http://localhost:8080).

## Deploying to Heroku

1) Create a new Heroku app:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command:
```
heroku logs --tail
```

_______

Other notes:

* To get a local environment going, ensure you've got both the snake AND the engine going.
## from docs:
## http://docs.battlesnake.io/zero-to-snake-linux.html


#start engine
cd ~/dev/battlesnake-2019/battlesnake-engine/
./engine dev

#start snake
cd ~/dev/battlesnake-2019/python-snake
#python3 app/main.py
gunicorn app.main:app
#or for with console output
PYTHONPATH=./ python app/main.py



* If the pytests are breaking and complaining about not being able to find the conftest.py file, 
delete the compiled python files in the projectsfind 
'''
. -name \*.pyc -delete
'''







## Contributors

* Jared Middleton (<jaredmiddleton3.14@gmail.com>)
* Matthew Casiro (<mattcasiro@gmail.com>)
