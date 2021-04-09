# ติดตั้ง Spark

## ดาวน์โหลด
```
cd;
cd downloads;
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
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME:$PATH:~/.local/bin:$JAVA_HOME/bin
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
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

## คำสั่ง Pyspark เบื้องต้น

```
import pyspark

pyspark.__version__

# spark = sql.SparkSession.builder.getOrCreate()
spark = pyspark.sql.SparkSession.builder.appName("YongyeeMaster").getOrCreate()

# sc_config = pyspark.SparkConf().setMaster('local').setAppName('YongyeeMaster')
# sc = pyspark.SparkContext(conf=sc_config).getOrCreate()
sc = spark.sparkContext

spark
sc

spark.stop()
sc.stop()
```