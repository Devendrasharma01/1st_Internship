def get_temperature():

  while True:
    try:
      temperature = float(input("Enter temperature: "))
      return temperature
    except ValueError:
      print("Invalid input. Please enter a number.")


def convert_temperature(temperature, from_unit, to_unit):

  if from_unit == "C" and to_unit == "F":
    return (temperature * 9/5) + 32
  elif from_unit == "F" and to_unit == "C":
    return (temperature - 32) * 5/9
  else:
    print("Invalid conversion direction. Please choose 'C' to 'F' or 'F' to 'C'.")
    return None


def main():

  while True:
    temperature = get_temperature()
    from_unit = input("Enter temperature unit (C or F): ").upper()
    to_unit = input("Enter conversion unit (C or F): ").upper()

    converted_temperature = convert_temperature(temperature, from_unit, to_unit)
    if converted_temperature is not None:
      print(f"{temperature}{from_unit} is equal to {converted_temperature:.2f}{to_unit}")

    choice = input("Do another conversion (y/n)? ").lower()
    if choice != "y":
      break



main()
