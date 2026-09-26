print("Program starting.")
fahrenheit = float(input("Insert fahrenheits: "))
celsius = (fahrenheit - 32) / 1.8
celsius_rounded = round(celsius, 1)
print(f"{fahrenheit}°F is {celsius_rounded}°C")
print("Program ending.")