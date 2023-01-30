name = (input("Name of Weather Station: "))

DegreesF = (float(input("\nWhat is the current temperature '(Fahrenheit)?': ")))

WindSpeed = (int(input("\nWhat is the wind speed?: ")))

WindDirection = (input("\nWhat is the wind direction?: "))

DegreesC = float(5/9 * (DegreesF-32))

name2 = (str(name+' Weather Station'))

print('\n')

print (f"{name2:>40}\n")
print (f"{'Temperature(Fahrenheit):' : >30}",f"{DegreesF:<15.1f}")
print (f"{'Temperature(Celsius):' : >30}",f"{DegreesC:<15.1f}")
print (f"{'Wind speed(mph):' : >30}", f"{WindSpeed:<15}")
print (f"{'Wind direction:' : >30}", f"{WindDirection:<15}")
