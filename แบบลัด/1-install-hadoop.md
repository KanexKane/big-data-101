## Create Hadoopuser

```
sudo -i
```

```
adduser hadoopuser
```

```
usermod -aG sudo hadoopuser
```

```
su hadoopuser
```

## Install packages

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
```

```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list;
sudo apt-get update;
;

```

```

sudo apt-get install -y git openjdk-8-jdk ssh pdsh mysql-server gnupg mongodb-org python3-venv

```

## Download files

```

cd;
mkdir downloads;
cd downloads;
;

```

```

git clone https://github.com/kanexkane/big-data-101;
git clone https://github.com/datacharmer/test_db;
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz;
wget http://mirrors.estointernet.in/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz;
wget http://apachemirror.wuchna.com/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz;
wget https://downloads.apache.org/commons/lang/binaries/commons-lang-2.6-bin.tar.gz;
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar;
;

```

```

tar -xzvf hadoop-3.3.0.tar.gz;
tar -xzvf apache-hive-3.1.2-bin.tar.gz;
tar -xzvf sqoop-1.4.7.bin\_\_hadoop-2.6.0.tar.gz;
tar -xzvf commons-lang-2.6-bin.tar.gz;
;

```

```

mv hadoop-3.3.0 /home/hadoopuser/hadoop;
mv sqoop-1.4.7.bin\_\_hadoop-2.6.0 /home/hadoopuser/sqoop;
mv apache-hive-3.1.2-bin /home/hadoopuser/hive;
cp commons-lang-2.6/commons-lang-2.6.jar /home/hadoopuser/sqoop/lib;
cp mysql-connector-java-8.0.23.jar /home/hadoopuser/sqoop/lib;
;

```

## Setting Hadoop

```

cp /home/hadoopuser/downloads/big-data-101/hadoop/etc/hadoop/* /home/hadoopuser/hadoop/etc/hadoop/;
cp /home/hadoopuser/downloads/big-data-101/hive/conf/* /home/hadoopuser/hive/conf/;
cp /home/hadoopuser/downloads/big-data-101/sqoop/conf/* /home/hadoopuser/sqoop/conf/;
rm -rf /home/hadoopuser/hive/lib/guava-19.0.jar;
cp /home/hadoopuser/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar /home/hadoopuser/hive/lib;
cp /home/hadoopuser/downloads/mysql-connector-java-8.0.23.jar /home/hadoopuser/hive/lib;
cp /home/hadoopuser/hive/lib/hive-common-3.1.2.jar /home/hadoopuser/sqoop/lib;
;

```

```

sudo chown hadoopuser:root -R /home/hadoopuser/hadoop

```

```

sudo chmod g+rwx -R /home/hadoopuser/hadoop

```

```

sudo chown -R hadoopuser:hadoopuser /home/hadoopuser/sqoop/lib/*

```

```

mkdir /home/hadoopuser/hadoop/data;
mkdir /home/hadoopuser/hadoop/data/namenode;
mkdir /home/hadoopuser/hadoop/data/datanode;
;

```

## Configure SSH

```

ssh-keygen -t rsa -P ""

```

```

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys;
ssh localhost;
;

```

## Configure Environment

```

sudo nano /etc/environment

```

```

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre

```

## Edit bashrc

```

sudo nano ~/.bashrc

```

```

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
export HADOOP_HOME=/home/hadoopuser/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_LIBEXEC_DIR=$HADOOP_HOME/libexec
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HADOOP_YARN_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export JAVA_LIBRARY_PATH=$HADOOP_HOME/lib/native:$JAVA_LIBRARY_PATH
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin

pdsh -q -w localhost

export PDSH_RCMD_TYPE=ssh

export SQOOP_HOME=/home/hadoopuser/sqoop
export PATH=$PATH:$SQOOP_HOME/bin

export HIVE_HOME=/home/hadoopuser/hive
export PATH=$PATH:$HIVE_HOME/bin

```

```

source ~/.bashrc

```

## Format file system

```

hdfs namenode -format

```

## Start Hadoop

```

start-dfs.sh
start-yarn.sh

# check jobs and node list

jps
yarn node -list

```

หลังจากสั่งสตาร์ท Hadoop แล้วสามารถเข้าผ่านเว็บบราวเซอร์ได้ที่ http://localhost:9870

## Stop Hadoop

```

stop-yarn.sh
stop-dfs.sh

```

## สร้าง Environment

```

cd;
mkdir bigdata;
cd bigdata;
python3 -m venv bigdata_env;
source bigdata_env/bin/activate;
python3 -m pip install --upgrade pip;
;

```

## ติดตั้งแพ็คเกจ Python ที่ใช้กับ Big Data

(bigdata_env):

```

pip3 install numpy pandas matplotlib seaborn sklearn pyspark pymongo handyspark;
python3 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python;
sudo apt install -y python3-notebook jupyter jupyter-core;
python3 -m pip install ipykernel;
;
```

```
python3 -m ipykernel install --user --name=bigdata_env;
jupyter notebook;
;
```

## สร้าง sqoopuser & hiveuser ใน MySQL

```

sudo mysql

```

```

CREATE DATABASE hadoop_test;
USE hadoop_test;
CREATE TABLE user (name VARCHAR(20));
CREATE USER "sqoopuser"@"localhost" IDENTIFIED BY "p@ssw0rd";
GRANT ALL PRIVILEGES ON hadoop_test.* TO "sqoopuser"@"localhost";
CREATE USER "hiveuser"@"localhost" IDENTIFIED BY "hivepassword";
GRANT ALL PRIVILEGES ON *.* TO "hiveuser"@"localhost";
FLUSH PRIVILEGES;
quit;
;

```

### การ import mysql test_db/employees

```

cd /home/hadoopuser/downloads/test_db;
sudo mysql -t < employees.sql;
;

```

## สร้างโฟลเดอร์ HIVE บน HDFS

```

hdfs dfs -mkdir /tmp;
hdfs dfs -mkdir -p /hive/warehouse;
hdfs dfs -chmod g+w /tmp;
hdfs dfs -chmod g+w /hive/warehouse;
;

```

## ทดลองสร้างฐานข้อมูล metastore ใน MySQL ผ่าน Hive tool

```

/home/hadoopuser/hive/bin/schematool -initSchema -dbType mysql

```

### คำสั่ง import ทุกๆ table จาก database ที่ต้องการใน mysql

#### แบบนี้คือแบบที่เคนไปหามาได้

sqoop import-all-tables --connect jdbc:mysql://localhost/employees --username hiveuser --password hivepassword --hive-import --hive-database employees --create-hive-table --direct -m 1

#### อันนี้คือแบบที่อาจารย์ให้มา

sqoop import-all-tables --connect jdbc:mysql://localhost/employees --username hiveuser --password hivepassword --direct -m 1

## เช็คว่า Import ไปที่ Hive เข้า Hdfs ไหม

```

hdfs dfs -ls /user/hadoopuser/;
hdfs dfs -cat /user/hadoopuser/departments/part-m-00000;
;

```

```

```

```

```
