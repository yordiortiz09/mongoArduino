import json
import serial
from pymongo import MongoClient
from HCSR04Sensor import HCSR04Sensor

class SensorData:
    def __init__(self, sensor_list):
        self.sensors = sensor_list
        self.serial_connection = None

    def connect_serial(self, port, baudrate):
        self.serial_connection = serial.Serial(port, baudrate)

    def read_sensors(self):
        for sensor in sensors:
            sensor.read(self.serial_connection)

    def to_json(self):
        data = {}
        for sensor in sensors:
           data[f"D{sensor.trigger_pin}"] = sensor.get_distance()
        return json.dumps(data)

    def to_mongodb(self, uri, database_name, collection_name):
        client = MongoClient(uri)
        database = client[database_name]
        collection = database[collection_name]
        data = {}
        for sensor in sensors:
          data[f"D{sensor.trigger_pin}"] = sensor.get_distance() 
        collection.insert_one(data)


if __name__ == "__main__":
    # Creamos una lista de sensores
    sensors = [HCSR04Sensor(8, 9), HCSR04Sensor(10, 11)]
    sensor_data = SensorData(sensors)
    sensor_data.connect_serial("COM6", 9600)
    sensor_data.read_sensors()
    while True:
        sensor_data.read_sensors()

        json_data = sensor_data.to_json()
        print(json_data)

   
        sensor_data.to_mongodb("mongodb+srv://yordiortiz98:Edition210302@cluster0.rcu24ht.mongodb.net/test", "test", "sensor_data")

    # reader.connect()
    # reader.read_sensors()
    # reader.save_to_database()
    # reader.disconnect()