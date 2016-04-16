# use docker-compose to manage these three containers, nginx, flask and mysql.
import interlock plugin to configure the procxy in nginx.
e.g [screenshot][screenshot]

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

### generate swarm token
$docker run --rm swarm create -> [SWARM_TOKEN]
### launch a manager node in local
$docker-machine create -d virtualbox --swarm --swarm-master --swarm-discovery token://[SWARM_TOCKEN] manager
### launch a client node in local
$docker-machine create -d virtualbox --swarm --swarm-discovery token://[SWARM_TOCKEN] node-01

## screenshot
![interlock with swarm](/screenshot/interlock_swarm.png "interlock_swarm")
