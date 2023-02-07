def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
centigrade = fahrenheit_to_centigrade(fahrenheit)
print(f"{fahrenheit}°F is equivalent to {centigrade}°C")
