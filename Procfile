release: cp config.prod.ini config.ini
web: gunicorn app.main:app --worker-class gevent
