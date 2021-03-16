## Install mysql

```
sudo apt update
sudo apt install mysql-server
```

# Command Service MySQL

```
sudo service mysql start
sudo service mysql stop
sudo service mysql status
sudo service mysql restart
```

## Install MongoDB

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

sudo apt-get install gnupg

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

sudo apt-get update

sudo apt-get install -y mongodb-org
```

# Command Service MongoDB

```
sudo service mongod start
sudo service mongod stop
sudo service mongod status
sudo service mongod restart
```
