import mysql.connector
import pymongo
import datetime

dbName = "hadoop_test"

mgoclient = pymongo.MongoClient("mongodb://localhost:27017")
mgodb = mgoclient[dbName]

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database=dbName
)

def migrate(db, mgodb, table, page):
    cursor = db.cursor(dictionary=True)
    limit = 100
    mgocol = mgodb[table]
    mgocol.create_index("ID", unique=True)

    while True:
        offset = (page - 1) * limit
        page = page + 1

        sql = "SELECT * FROM " + table + " LIMIT " + str(offset) + "," + str(limit)
        cursor.execute(sql)

        result = cursor.fetchall()
        
        if(len(result) <= 0):
            break

        for row in result:
            for key in row:
                if(isinstance(row[key], datetime.datetime) or isinstance(row[key], datetime.date)):
                    row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')

            try:
                mgocol.insert_one(row)
            except:
                print("Error Insert")


mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()

for table in tables:
    print(table)
    migrate(db, mgodb, table[0], 1)

print("DONE")