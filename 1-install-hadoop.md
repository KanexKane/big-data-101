## Create Hadoopuser

```
sudo -I
adduser hadoopuser
usermod -aG sudo hadoopuser
```

## Install Java

```
sudo apt-get install openjdk-8-jdk
java -version
```

## Install ssh and pdsh

```
sudo apt-get install ssh pdsh
```

## Download hadoop

```
cd
mkdir Downloads
cd Downloads
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
tar -xzvf hadoop-3.3.0.tar.gz
mv hadoop-3.3.0 /home/hadoopuser/hadoop
```

## Setting Hadoop

```
cd /home/hadoopuser/hadoop/etc/hadoop
```

เอาไฟล์จากโฟลเดอร์ hadoop/etc/hadoop ก๊อบปี้ใส่เข้าไปได้เลย หรือจะก๊อบโค้ดตรงนี้ใส่ทีละไฟล์ก็ได้

### core-site.xml

```
sudo nano core-site.xml
```

```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

### hdfs-site.xml

```
sudo nano hdfs-site.xml
```

```
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/hadoopuser/hadoop/data/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.name.dir</name>
        <value>/home/hadoopuser/hadoop/data/datanode</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### mapred-site.xml

```
sudo nano mapred-site.xml
```

```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```

### yarn-site.xml

```
sudo nano mapred-site.xml
```

```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

### hadoop-env.sh

```
sudo nano hadoop-env.sh
```

```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

## Configure SSH

```
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
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
sudo chown hadoopuser:root -R /home/hadoopuser/hadoop
sudo chmod g+rwx -R /home/hadoopuser/hadoop
```

## Format file system

```
cd $HADOOP_HOME
mkdir data
mkdir data/namenode
mkdir data/datanode
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
stop-dfs.sh
stop-yarn.sh
```
