# ติดตั้ง Spark

## ดาวน์โหลด
```
cd /downloads;
wget https://downloads.apache.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop2.7.tgz;
tar -xzvf spark-3.1.1-bin-hadoop2.7.tgz;
mv spark-3.1.1-bin-hadoop2.7 /home/hadoopuser/spark;
;
```

## แก้ไฟล์ .bashrc
```
sudo nano ~/.bashrc
```
เพิ่มโค้ดชุดนี้ไว้ด้านบนของ pdsh -q -w localhost
```
export SPARK_HOME=/home/hadoopuser/spark/
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME:$PATH:~/.local/bin:$JAVA_HOME/bin
```
```
source ~/.bashrc
```

## Activate Environment
```
source /bigdata/bigdata_env/bin/activate
```

## Run Pyspark
(bigdata_env):
```
pyspark
```