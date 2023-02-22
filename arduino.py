import serial
import json
from pymongo import MongoClient

import pymongo

client = pymongo.MongoClient("mongodb+srv://yordiortiz98:Edition210302@cluster0.rcu24ht.mongodb.net/test")
db = client["mydata"]

col = db["temperatura"]

ser = serial.Serial('COM5', 9600) 
while True:
    if ser.in_waiting > 0:
        try:
            temperatura = float(ser.readline().decode('utf-8'))
            print(temperatura)
            data = {"temperatura": temperatura}
            data_json = json.dumps(data) 
            col.insert_one(json.loads(data_json)) 
        except ValueError:
            print("El valor de temperatura no es numérico")
      
    