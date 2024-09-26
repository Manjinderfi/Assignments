airports = {}

while True:
    print("1. Enter new airport")
    print("2. Fetch airport info")
    print("3. Quit")

    choice = input()

    if choice == '1':
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name

    elif choice == '2':
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found")

    elif choice == '3':
        break

    else:
        print("Invalid choice")
