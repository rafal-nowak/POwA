class Sensor:
    def read(self):
        pass

class TemperatureSensor(Sensor):
    def read(self):
        return "Temperature: 25°C"

class SensorFactory:
    @staticmethod
    def create_sensor(sensor_type):
        if sensor_type == "temperature":
            return TemperatureSensor()
        raise ValueError("Unknown sensor type")

if __name__ == "__main__":
    # Przykład użycia
    sensor = SensorFactory.create_sensor("temperature")
    print(sensor.read())