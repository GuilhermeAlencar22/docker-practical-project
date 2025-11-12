docker build -t flask-server ./web
docker build -t curl-client ./client

docker network inspect rede-flask >/dev/null 2>&1 || docker network create rede-flask
docker run -d --name web --network rede-flask -p 8080:8080 flask-server
docker run -d --name client --network rede-flask curl-client
