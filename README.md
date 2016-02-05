# [Flask example](http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972)

# try run with uWSGI
$uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi -H venv --callable app

# production ru with uWSGI
$uwsgi --ini wsgi.ini
