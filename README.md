# use docker-compose to manage these three containers, nginx, flask and mysql.
right now only support 1-1, (nginx <-> web)

## run docker compose with daemon
$ docker-compose up -d nginx

#reference
## [Flask example](http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972)

## develop run with uWSGI
$uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi -H ../../venv --callable app

## production run with uWSGI
$uwsgi --ini wsgi.ini

## pack mysql database, BucketList, into docker container
$mysqldump -u root -p BucketList --routines > BucketList.sql
$mysql -u root -p -h [192.168.64.3] < mysql-allTables.sql

## [docker swarm](https://blog.codeship.com/docker-machine-compose-and-swarm-how-they-work-together/)
