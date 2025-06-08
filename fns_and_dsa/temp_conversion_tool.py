FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
f_or_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


def convert_to_celsius(fahrenheit):
    fahrenheit = temp
    celsius_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius_temp}°C")

def convert_to_fahrenheit(celsius):
    celsius = temp
    fahrenheit_temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit_temp}°F")

match f_or_c:
    case "C":
        convert_to_fahrenheit(temp)

    case "F":
        convert_to_celsius(temp)

    case _:
        print("Please choose the right option")