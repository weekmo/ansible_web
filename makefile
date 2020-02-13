clean: stop remove

stop:
	docker stop "$(docker ps -qa)"

remove:
	docker rm "$(docker ps -qa)"

build:
	docker build -t ansible_web .
