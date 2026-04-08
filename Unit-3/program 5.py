#temperature conversion class
class Temperature:
    def convert_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def convert_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

t = Temperature()
print("100°C to °F:", t.convert_fahrenheit(100))
print("212°F to °C:", t.convert_celsius(212))
