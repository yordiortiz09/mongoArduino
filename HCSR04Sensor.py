class HCSR04Sensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.distance = 0

    def begin(self, serial_connection):
        serial_connection.write(f"B{self.trigger_pin}:{self.echo_pin}\n".encode())

    def read(self, serial_connection):
        serial_connection.write(f"R{self.trigger_pin}:{self.echo_pin}\n".encode())
        response = serial_connection.readline().decode().strip()
        if response != "":
            name, value = response.split(':')
            if name == f"D{self.trigger_pin}":
                self.distance = float(value)

    def get_distance(self):
        return self.distance