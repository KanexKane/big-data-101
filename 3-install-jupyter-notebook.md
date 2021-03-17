(bigdata_env): <== พิมพ์คำสั่งขณะอยู่ใน Environmetn bigdata_env
(hadoopuser@...): <=== พิมพ์คำสั่งขณะเป็น hadoopuser

## เช็คว่ามี Python3.8

```
python3
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
```

## สร้าง Environment

```
cd
mkdir bigdata
cd bigdata
(hadoopuser@...): python3.8 -m venv bigdata_env
```

ตรงนี้หากขึ้น Error ว่าให้ install อะไร ก็ให้ install ตามนั้น อาจจะเป็นตัว apt install python3.8-venv หรือ apt-get install python3-venv จากนั้นก่อนไปต่อ ให้พิมพ์คำสั่ง rm -rf bigdata_env ลบออกไปก่อนเพราะในเมื่อมันมี Error มันถือว่าไม่สมบูรณ์

```
(hadoopuser@...): cd bigdata_env/bin
(hadoopuser@...): source activate
(bigdata_env):cd
(bigdata_env): python
(hadoopuser@...): python3.8 -m pip install --upgrade pip
(hadoopuser@...): source bigdata/bigdata_env/bin/activate
```

## สรุปคำสั่งที่ใช้ในการใช้งาน Environment

```
source bigdata/bigdata_env/bin/activate
```

## ติดตั้งแพ็คเกจ Python ที่ใช้กับ Big Data

```
(bigdata_env): pip3 install numpy pandas matplotlib seaborn sklearn pyspark pymongo handyspark
```

## ติดตั้ง MySQL Connector ของ Python

```
(bigdata_env): python3.8 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python
```

## Install Jupyter Notebook

```
(bigdata_env): sudo apt install python3-notebook jupyter jupyter-core
(bigdata_env): python3.8 -m pip install ipykernel
(bigdata_env): python3.8 -m ipykernel install --user --name=bigdata_env
```

## Run Jupyter notebook

```
(bigdata_env): jupyter notebook
```
