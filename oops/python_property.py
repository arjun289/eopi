class Celsius:
    def __init__(self, value=0):
        self._temperature = value

    def to_farenheit(self):
        return (self._temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print("Getting temp value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting temp value")
        self._temperature = value


human = Celsius(37)
print(human.temperature)

human.temperature = 36

print(human.temperature)