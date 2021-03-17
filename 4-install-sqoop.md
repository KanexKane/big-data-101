# ขั้นตอนการติดตั้ง Sqoop

ต้องแน่ใจว่าเป็น User สำหรับ hadoop แล้ว หากยังไม่ได้เป็นให้พิมพ์คำสั่งด้านล่างเพื่อเปลี่ยน User เป็นใน 1-install-hadoop

```
su hadoopuser
```

## ติดตั้ง Sqoop

```
cd /home/hadoopuser/Downloads
wget http://mirrors.estointernet.in/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
tar -xzvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
sudo mv sqoop-1.4.7.bin__hadoop-2.6.0 /home/hadoopuser/sqoop
```

## สร้าง sqoopuser ใน MySQL

```
sudo mysql
CREATE DATABASE hadoop_test;
USE hadoop_test;
CREATE TABLE user (name VARCHAR(20));
CREATE USER ‘sqoopuser’@‘localhost’ IDENTIFIED BY ‘p@ssw0rd’;
GRANT ALL PRIVILEGES ON hadoop_test.* TO ‘sqoopuser’@‘localhost’;
FLUSH PRIVILEGES;
quit;
```

## ทดสอบเข้า sqoopuser ที่เพิ่งสร้าง

```
mysql -u sqoopuser -p
USE hadoop_test;
INSERT INTO user VALUES ("sqoopuser"), ("hiveuser"), ("hadoopuser"), ("piguser"), ("mysqluser"), ("mongodbuser"), ("hbaseuser"), ("root");
SELECT * FROM user;
quit;
```

## แก้ bashrc

```
sudo nano ~/.bashrc
```

```
export SQOOP_HOME=/home/hadoopuser/sqoop
export PATH=$PATH:$SQOOP_HOME/bin
```

```
source ~/.bashrc
```

## ดาวน์โหลด Lib commons-lang ที่ Sqoop ต้องการ

```
cd /home/hadoopuser/Downloads
wget https://downloads.apache.org/commons/lang/binaries/commons-lang-2.6-bin.tar.gz
tar -xzvf commons-lang-2.6-bin.tar.gz
cd commons-lang-2.6
sudo cp commons-lang-2.6.jar $SQOOP_HOME/lib
```

## ดาวน์โหลด Lib mysql-connector-java ที่ Sqoop & Hive ต้องการ

ไฟล์ mysql-connector-java-8.0.23.jar อันนี้จะต้องใช้ทั้ง Sqoop และ Hive เก็บไว้ให้ดี

```
cd /home/hadoopuser/Downloads
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar
sudo cp mysql-connector-java-8.0.23.jar $SQOOP_HOME/lib
```

## เปลี่ยนเจ้าของ Sqoop/lib

```
sudo chown -R hadoopuser:hadoopuser /home/hadoopuser/sqoop/lib/*
```

## ทดลองส่งออกข้อมูลจาก MySQL ไปที่ HDFS ด้วย Sqoop

อันนี้จะเป็นแค่ Table เดียว

```
sqoop import --connect jdbc:mysql://localhost/hadoop_test —username ‘sqoopuser’ —password ‘p@ssw0rd’ —table user -m 1
hdfs dfs -cat user/*
```

อันนี้จะเป็นทุกๆ Table ของ Database เลย

```
sqoop import-all-tables --connect jdbc:mysql://localhost/hadoop_test --username ‘sqoopuser’ —password p@ssw0rd --direct -m 1
```
