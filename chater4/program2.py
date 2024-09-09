# Program to convert inches to centimeters until a negative value is entered

CONVERSION_FACTOR = 2.54

while True:
    inches = float(input("Enter a value in inches (or a negative number to stop): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * CONVERSION_FACTOR

    print(f"{inches} inches is equal to {centimeters} centimeters.")
