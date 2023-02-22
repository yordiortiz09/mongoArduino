import serial
from pymongo import MongoClient

ser = serial.Serial('COM5', 9600) 

client = MongoClient('mongodb+srv://yordiortiz98:Edition210302@cluster0.rcu24ht.mongodb.net/test', 27017) 
db = client['Arduino']
collection = db['sensores'] 

while True:
    line = ser.readline().decode().strip()
    print(line)
    data = {}
    for item in line.split(','):
        key, value = item.split(':')
        data[key.strip()] = value.strip()

   
    collection.insert_one(data)