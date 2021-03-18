# ติดตั้ง HIVE

## ดาวน์โหลดฐานข้อมูลจำลอง

แล้วทำการ Import เข้า mysql

```
sudo apt install git
cd /home/hadoopuser/downloads
git clone https://github.com/datacharmer/test_db
cd test_db
sudo mysql
CREATE DATABASE employees;
USE employees;
SOURCE employees.sql;
quit;
```

## ดาวน์โหลด HIVE

```
cd /home/hadoopuser/downloads
wget http://apachemirror.wuchna.com/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
tar -xzvf apache-hive-3.1.2-bin.tar.gz
sudo mv apache-hive-3.1.2-bin /home/hadoopuser/hive
```

## แก้ไข bashrc

```
sudo nano ~/.bashrc
```

```
export HIVE_HOME=/home/hadoopuser/hive
export PATH=$PATH:$HIVE_HOME/bin
```

```
source ~/.bashrc
```

## สร้างโฟลเดอร์ HIVE บน HDFS

```
hdfs dfs -mkdir /tmp
hdfs dfs -mkdir -p /hive/warehouse
hdfs dfs -chmod g+w /tmp
hdfs dfs -chmod g+w /hive/warehouse
```

## แก้ไขไฟล์ hive-env.sh

```
cd $HIVE_HOME/conf
sudo cp hive-env.sh.template hive-env.sh
sudo nano hive-env.sh
```

```
export HADOOP_HOME=/home/hadoopuser/hadoop
export HIVE_CONF_DIR=/home/hadoopuser/hive/conf
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
```

## สร้าง hiveuser ใน MySQL

```
sudo mysql
CREATE USER "hiveuser"@"localhost" IDENTIFIED BY "hivepassword";
GRANT ALL PRIVILEGES ON *.* TO "hiveuser"@"localhost";
FLUSH PRIVILEGES;
quit;
```

## แก้ไขไฟล์ hive-site.xml

```
cd $HIVE_HOME/conf
sudo cp hive-default.xml.template hive-site.xml
sudo nano hive-site.xml
```

### แก้ไขค่าเหล่านี้ในไฟล์ hive-site.xml

วิธีการหาให้กด Ctrl+W พิมพ์คำที่ค้นหาและกด Enter หาคำต่อไปให้กด Window+W หรือ Mac คือ Option+W

```
name: javax.jdo.option.connectionURL
value: jdbc:mysql://localhost/metastore?createDatabaseIfNotExist=true

name: javax.jdo.option.connectionDriverName
value: com.mysql.cj.jdbc.Driver

name: javax.jdo.option.connectionUsername
value: hiveuser

name: javax.jdo.option.connectionPassword
value: hivepassword

name: hive.txn.xlock.iow (ประมาณบรรทัดที่ 3219) ลบตัวอักขระ &#8; ออกจาก description
```

### เพิ่มค่าเหล่านี้ในไฟล์ hive-site.xml

```
<property><name>system:java.io.tmpdir</name><value>/tmp/hive/java</value></property>

<property><name>system:user.name</name><value>${user.name}</value></property>
```

## รัน hive และแก้ Error

```
hive
```

แล้วมันจะต้อง Error: Exception in thread “main” java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument(ZLjava/lang/String;Ljava/lang/Object;)V

มันคือการ Error ไฟล์ guava ก็ให้ก๊อบปี้จาก hadoop ไปใช้ใน hive

และอีกตัวนึงคือ มันจะ Error ตัว Connector มันใช้ไม่ได้ ให้ทำเหมือนกันคือเอาไฟล์ mysql-connector-java-8.0.23 ที่เคยดาวน์โหลดตอน Sqoop ก๊อบปี้ไปใส่ใน Hive ทำไปพร้อมกันเลยแล้วกัน

```
rm -rf $HIVE_HOME/lib/guava-19.0.jar
sudo cp $HADOOP_HOME/share/hadoop/common/lib/guava-27.0-jre.jar $HIVE_HOME/lib
sudo cp /home/hadoopuser/downloads/mysql-connector-java-8.0.23.jar $HIVE_HOME/lib
```

## สร้างฐานข้อมูล metastore ใน MySQL ผ่าน Hive tool

```
$HIVE_HOME/bin/schematool -initSchema -dbType mysql
```

## ทดสอบ Import จาก MySQL -> Hive ด้วย Sqoop

### สร้าง Database รอไว้ก่อนใน Hive

```
hive
CREATE DATABASE employees;
quit;
```

คำสั่ง import ทุกๆ table จาก database ที่ต้องการใน mysql

```
sqoop import-all-tables ––connect jdbc:mysql://localhost/employees ––username "hiveuser" ––password "hivepassword" ––hive-import ––hive-database employees ––create-hive-table -m 1
```

มันจะต้อง Error: hive.HiveConfig: Could not load org.apache.hadoop.hive.conf.HiveConf. Make sure HIVE_CONF_DIR is set correctly

### แก้ Error HIVE_CONF_DIR

```
cd $SQOOP_HOME/conf
sudo cp sqoop-env-template.sh sqoop-env.sh
sudo nano sqoop-env.sh
```

```
export HIVE_HOME=/home/hadoopuser/hive
export HIVE_CONF_DIR=/home/hadoopuser/hive/conf
```

```
cd $HIVE_HOME/lib
sudo cp hive-common-3.1.2.jar $SQOOP_HOME/lib
```

### รันคำสั่ง Import อีกครั้ง

```
sqoop import-all-tables ––connect jdbc:mysql://localhost/employees ––username "hiveuser" ––password "hivepassword" ––hive-import ––hive-database employees ––create-hive-table -m 1
```

```
hive
USE employees;
SELECT * FROM departments;
```
