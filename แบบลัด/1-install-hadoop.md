## Create Hadoopuser

```
sudo -i
adduser hadoopuser
```

```
usermod -aG sudo hadoopuser;
su hadoopuser;
```

## Install Java

```
sudo apt-get update;
sudo apt-get install -y git openjdk-8-jdk ssh pdsh mysql-server gnupg python3-venv;
```

## Download hadoop

```
cd;
mkdir downloads;
cd downloads;
git clone https://github.com/kanexkane/big-data-101;
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz;
tar -xzvf hadoop-3.3.0.tar.gz;
mv hadoop-3.3.0 /home/hadoopuser/hadoop;
```

## Setting Hadoop

```
sudo cp /home/hadoopuser/downloads/hadoop/etc/hadoop/* /home/hadoopuser/hadoop/etc/hadoop/
```

## Configure SSH

```
ssh-keygen -t rsa -P "";
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys;
ssh localhost
```

## Configure Environment

```
sudo nano /etc/environment
```

```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
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
```

```
source ~/.bashrc
```

## Configure Owner and mode of hadoop directory

```
sudo chown hadoopuser:root -R /home/hadoopuser/hadoop;
sudo chmod g+rwx -R /home/hadoopuser/hadoop;
```

## Format file system

```
mkdir $HADOOP_HOME/data;
mkdir $HADOOP_HOME/data/namenode;
mkdir $HADOOP_HOME/data/datanode;
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

## Install MongoDB

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -;

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list;

sudo apt-get update;

sudo apt-get install -y mongodb-org;
```

## สร้าง Environment

```
cd;
mkdir bigdata;
cd bigdata;
python3 -m venv bigdata_env;
source bigdata_env/bin/activate;
python3 -m pip install --upgrade pip;
```

## ติดตั้งแพ็คเกจ Python ที่ใช้กับ Big Data

```
(bigdata_env): pip3 install numpy pandas matplotlib seaborn sklearn pyspark pymongo handyspark;
python3 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python;
sudo apt install python3-notebook jupyter jupyter-core;
python3 -m pip install ipykernel;
python3 -m ipykernel install --user --name=bigdata_env
```
