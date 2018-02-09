

git clone https://github.com/spulec/moto
docker build --tag moto moto
# add 0.0.0.0 swf.aws.local to hosts file
docker-compose up -d 
copy .boto ~/
make setup
make test