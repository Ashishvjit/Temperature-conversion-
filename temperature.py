def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

print("Select conversion:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter choice (1/2): ")

if choice in ('1', '2'):
    temperature = float(input("Enter temperature: "))

    if choice == '1':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {result:.2f} Celsius")

    elif choice == '2':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {result:.2f} Fahrenheit")

else:
    print("Invalid Input")
