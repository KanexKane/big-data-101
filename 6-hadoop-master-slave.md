# Hadoop Master-Slave

## ตั้งค่า Network ของ Virtual Box บน Mac

- ไปที่ Files -> Host Network Manager
- กด Create
- กดติ๊กถูกที่ Server DHCP
- ไปที่ Virtual Machine ที่ต้องการ กดคลิกขวาเลือก ตั้งค่า
- ไปที่ Network (เครือข่าย)
- เลือก แผงวงจรเฉพาะโฮสต์ ภาษาอังกฤษน่าจะ Host-only Device
- เลือกชื่อที่เพิ่งสร้างขึ้นมา

## ทำการโคลน Virtual Machine

- คลิกขวาที่ Virtual Machine ที่ต้องการ แล้วเลือก Clone
- ตั้งชื่อ แล้วกด Next
- เลือกแบบ Full Clone (โคลนทั้งหมด)

## แก้ไข Mac Address ของ Network

- ไปที่ Virtual Machine ที่ต้องการ กดคลิกขวาเลือก ตั้งค่า
- ไปที่ Network (เครือข่าย)
- กดแสดงส่วนของ Advanced ออกมา แล้วกดปุ่มรีเฟรชตรงหลัง Mac Address เพื่อให้ค่าแต่ละ VM เป็นคนละค่ากัน

## เปลี่ยน hostname

ส่วนนี้ให้ทำทีละเครื่องโดยทำที่ตัวหลักก่อน เช่น หากมี 3 เครื่อง คือ 1 เครื่องหลัก และ 2 เครื่องย่อย
จะกำหนดชื่อตามนี้เพื่อง่ายต่อการจดจำ

- sujanya-primary
- sujanya-secondary1
- sujanya-secondary2

ก็ให้เข้าไปที่ VM แต่ละตัวและทำการแก้ไขไฟล์ด้วยคำสั่ง

```
sudo nano /etc/hostname
```

แล้วพิมพ์ชื่อที่ต้องการเข้าไป โดยหลังจากกดบันทึกแล้วให้ทำการรีสตาร์ทเครื่องด้วยคำสั่ง

```
sudo reboot
```

### เช็ค IP แต่ละเครื่อง

```
ip addr
```

แล้วมองหาตรง inet ว่าเป็น 192.168.?.? อะไร ตัวอย่าง 192.168.1.56.101 - 192.168.1.56.103

พอได้แต่ละเครื่องมาแล้ว เราจะเอา IP แต่ละเครื่องมาแก้ไขในไฟล์ hosts

```
sudo nano /etc/hosts
```

แล้วเพิ่ม IP และชื่อเครื่องเข้าไป

```
192.168.56.101  sujanya-primary
192.168.56.102  sujanya-secondary1
192.168.56.103  sujanya-secondary2
```

## ก๊อปปี้ ssh จากเครื่องหลักไปเครื่องย่อย

หากยังไม่เคยสร้าง ssh key มาก่อน หรือไม่แน่ใจ ให้กดสร้างใหม่โดยเขียนทับของเดิม

```
ssh-keygen -t rsa
```

จากนั้นสั่งก๊อปปี้ไปทุกเครื่อง

```
ssh-copy-id hadoopuser@sujanya-primary
ssh-copy-id hadoopuser@sujanya-secondary1
ssh-copy-id hadoopuser@sujanya-secondary2
```

## แก้ไข core-site.xml

```
sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

```
<property>
    <name>fs.defaultFS</name>
    <value>hdfs://sujanya-primary:9000</value>
</property>
```

## แก้ไข hdfs-site.xml

```
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

แก้ไขแค่ส่วน dfs.replication น่าจะปรับตามจำนวนเครื่องย่อย หากมีเครื่องย่อย 5 ก็ให้ใส่ค่าเป็น 5

```
<property>
    <name>dfs.replication</name>
    <value>2</value>
</property>
```

## แก้ไข workers ทุกเครื่อง

```
sudo nano $HADOOP_HOME/etc/hadoop/workers
```

```
sujanya-secondary1
sujanya-secondary2
```

## ทดลองรัน start-dfs.sh

หลังจากสั่งรัน ลองเข้าไปที่ 192.168.56.101:9870 ไปดูที่ Live Node หากถูกต้องมันต้องมีค่าเป็น 2 หรือในส่วนของ Datanode ต้องมีรายการเครื่องย่อยแสดงขึ้นมา

## เช็คด้วยคำสั่ง jps

หรือลองเช็คด้วยคำสั่ง jps แต่ละเครื่องดูว่า DataNode มันทำงานไหม

## แก้ไข yarn-site.xml เฉพาะเครื่องย่อยทั้ง 2 เครื่อง

```
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

ให้เหลือแค่โค้ดชุดนี้

```
<property>
    <name>yarn.resourcemanager.hostname</name>
    <value>sujanya-primary</value>
</property>
```

## ทดลองรัน start-yarn.sh

หลังจากสั่งรัน ลองเข้าไปที่ 192.168.56.101:8088 ไปดูที่ Active Node หากถูกต้องมันต้องมีค่าเป็น 2
