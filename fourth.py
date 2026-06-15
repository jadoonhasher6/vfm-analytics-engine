def convert_temperature(celcius):
    fahernheit =celcius * 9/5 + 32
    kelvin = celcius + 273.15
    return fahernheit,kelvin
f_temp, k_temp = convert_temperature(25)
print(f"Fahrenheit: {f_temp}, Kelvin: {k_temp}")

print(f"Original: 25°C")
print(f"In Fahrenheit: {f_temp}°F")
print(f"In Kelvin: {k_temp}K")