## เช็คว่ามี Python3.8

```
python3
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
python3.8 -m pip install --upgrade pip
```

## สร้าง Environment

```
sudo apt install python3.8-venv
cd
mkdir bigdata
cd bigdata
python3.8 -m venv bigdata_env
cd bigdata_env/bin
source activate
python
```

## สรุปคำสั่งที่ใช้ในการใช้งาน Environment

```
source bigdata/bigdata_env/bin/activate
```

## ติดตั้งแพ็คเกจ Python ที่ใช้กับ Big Data

ต้องทำการ Activate ให้เป็น Environment ของ (bigdata_env) ก่อน

```
pip3 install numpy pandas matplotlib seaborn sklearn pyspark pymongo handyspark
```

## ติดตั้ง MySQL Connector ของ Python

Activate (bigdata_env)

```
python3.8 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python
```

## Install Jupyter Notebook

Activate (bigdata_env)

```
sudo apt install python3-notebook jupyter jupyter-core
python3.8 -m pip install ipykernel
python3.8 -m ipykernel install --user -- name=bigdata_env
```

## Run Jupyter notebook

```
jupyter notebook
```
