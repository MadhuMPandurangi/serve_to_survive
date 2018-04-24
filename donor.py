from random import randint
from pymongo import MongoClient

conn = MongoClient()
db = conn.donorData

collection = db.donor

emp_rec1 = {
    "name": "Mr.Geek",
    "eid": 24,
    "location": "delhi"
}



rec_id1 = collection.insert_one(emp_rec1)

print("Data inserted with record ids",  rec_id1)


cursor = collection.find()
for record in cursor:
    print(record)