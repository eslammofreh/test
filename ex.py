cToK = 273.15
def checkValidity(unit, temp):
    if unit == "F" and (temp < -459.67 or toCelsuius(temp) < -273.15):
        return False;
    elif unit == "C" and (temp < 0 or toFahrenheit(temp) < -459.67):
        return False;
    elif unit == "K" and (temp < -459.67 or toCelsuius(temp) < -273.15):
        return False;

def toFahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

def toCelsuius(temperature):
    return (temperature - 32) * (5 / 9)

def convert_temperature(temperature, unit):
    if unit == "F":  
        if not checkValidity(unit, temperature):
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            return celsius, kelvin
    elif unit == "C":
        if not checkValidity(unit, temperature):
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return fahrenheit, kelvin
    elif unit == "K":
        if not checkValidity(unit, temperature):
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = toFahrenheit(celsius)
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, fahrenheit
    else:
        return "Invalid unit"

# to run
if __name__ == "__main__":
    print(convert_temperature(0, "C"))