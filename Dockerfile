FROM ubuntu

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update -y && apt upgrade -y && apt install python3 python3-pip ansible redis-server -y
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["service", "redis-server", "start"]