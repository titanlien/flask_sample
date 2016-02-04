# [Flask example](http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972)

# run with nginx
$uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi -H venv --callable app
