# docker-compose, docker-swarm to manage these containers, nginx, interlock, flask and mysql.
import interlock plugin to configure the procxy in nginx.
e.g screenshot

## run docker compose with daemon
$ docker-compose up -d nginx

## develop run with uWSGI
$uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi -H ../../venv --callable app

## production run with uWSGI
$uwsgi --ini wsgi.ini

## pack mysql database, BucketList, into docker container
$mysqldump -u root -p BucketList --routines > BucketList.sql
$mysql -u root -p -h [192.168.64.3] < mysql-allTables.sql

## [docker swarm](https://blog.codeship.com/docker-machine-compose-and-swarm-how-they-work-together/)
## swarm local
### generate swarm token
$docker run --rm swarm create -> [SWARM_TOKEN]
### launch a manager node in local
$docker-machine create -d virtualbox --swarm --swarm-master --swarm-discovery token://[SWARM_TOCKEN] manager
### launch a client node in local
$docker-machine create -d virtualbox --swarm --swarm-discovery token://[SWARM_TOCKEN] node-01
### export swarm manager environment
$eval $(docker-machine env --swarm manager)
### verify the swarm setting
$docker info

## swarm google
### launch google cloud container 
#### watch out, you should modify the /etc/systemd/system/docker.service like below setting
ExecStart=/usr/bin/docker daemon -H tcp://0.0.0.0:2376 -H unix:///var/run/docker.sock --storage-driver aufs --tlsverify --tlscacert /etc/docker/ca.pem --tlscert /etc/docker/server.pem --tlskey /etc/docker/server-key.pem --label provider=google
#### kvs -> consul
$docker-machine create --driver google --google-project flask-titan --google-zone us-central1-a --google-machine-type f1-micro flask-kvs

$docker $(docker-machine config flask-kvs) run -d -p "8500:8500" -h "consul" progrium/consul -server -bootstrap

#### manager
$docker-machine create -d google -google-project flask-titan --google-zone us-central1-a --google-machine-type f1-micro --google-tags manager --swarm --swarm-master --swarm-discovery="consul://$(docker-machine ip flask-kvs):8500" --engine-opt="cluster-store=consul://$(docker-machine ip flask-kvs):8500" --engine-opt="cluster-advertise=eth0:2376" g-manager

#### node, [HINT] you could use first node's snapshot to create the other nodes' disk.
$docker-machine create -d google -google-project flask-titan --google-zone us-central1-a --google-machine-type f1-micro --google-tags node --swarm --swarm-discovery="consul://$(docker-machine ip flask-kvs):8500" --engine-opt="cluster-store=consul://$(docker-machine ip flask-kvs):8500" --engine-opt="cluster-advertise=eth0:2376" g-node-01

### reference
#### [Flask example](http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972)
#### [docker-machine & swarm on google](https://crate.io/a/deploying-crate-with-docker-machine-swarm/)
#### [docker-machine & consul & swarm](http://mix-juice001.hatenablog.com/entry/2016/02/02/000057)


## screenshot
### local virtualbox
![interlock with swarm](/screenshot/interlock_swarm.png "interlock_swarm")
### google cloud
![google swarm & consul](/screenshot/googlo-swarm-consul.png "gcloud + swarm + kvs")
### compose (2.0) + interlock + flask + consul + gcloud
