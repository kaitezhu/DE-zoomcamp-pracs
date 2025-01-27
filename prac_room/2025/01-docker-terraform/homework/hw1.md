## Question 1. Version of pip

(base) ktzhu@KaitedeMBP 1_docker_sql % docker run -it --entrypoint=bash python:3.12.8

root@bf6070e95d49:/# pip -V
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

Answer: 24.3.1

## Question 2. Docker networking and docker-compose

The hostname is essentially the service name provided in the yaml file, (in this case db), services can communicate with each other using hostnames.
We use ports from the container (5432) to communicate instead of the mapped port. So db:5432.

Answer: db:5432
