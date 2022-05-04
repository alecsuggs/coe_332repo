build:
	docker build -t alecsuggs/app:1.0 .

run:
	docker run --name "ISStrackerapp" -p 5033:5000 alecsuggs/app:1.0

stop:
	docker stop "ISStrackerapp"

image:
	docker images | grep alecsuggs

remove:
	docker rm "ISStrackerapp"

pull:
	docker pull alecsuggs/app:1.0

removei:
	docker rmi alecsuggs/app:1.0

