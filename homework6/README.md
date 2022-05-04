
# Kubernetes Flask Application with Redis database

## How to deploy the software systems in Kubernetes:

Fist make sure that all five of the YAML files are inside the kubernetes instance.

1. asuggs-test-flask-deployment.yml
2. asuggs-test-flask-service.yml
3. asuggs-test-redis-deployemnt.yml
4. asuggs-test-redis-pvc.yml
5. asuggs-test-redis-service.yml

After confirming that all five of the files are inside the kubernetes instance
follow these commands to start the flask app:

First start the redis persistent volume claim:

`kubectl apply -f asuggs-test-redis-pvc.yml`

Next start the redis deployment:

`kubectl apply -f asuggs-test-redis-deployment.yml`

Then create a redis service:

`kubectl apply -f asuggs-test-redis-service.yml`

The redis database should now be deployed into kubernetes. Now it is 
time to start the flask application. 

Start up the flask app deployment:

`kubectl apply -f asuggs-test-flask-deployment.yml`

Then start the flask service:

`kubectl apply -f asuggs-test-flask-service.yml`

The flask app and redis database should now be containerized and running
on the kubernetes instance.
