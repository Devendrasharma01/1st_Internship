def convert_temperature(temp,from_unit):
    if from_unit.lower() == "celsius":
        return (temp * 9/5) + 32
    elif from_unit.lower() == "fahrenheit":
        return (temp - 32) * 5/9
    else:
        return "Invalid unit.."
    
temp = float(input("Enter the temperature: "))
from_unit = input("Enter the current unit (Celsius/Fahrenheit): ")

convert_temp = convert_temperature(temp,from_unit)
print(f"The temperature is {convert_temp}")