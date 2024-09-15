def city_names():
    cities = []

    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)  # Add the city name to the list

    print("\nThe cities you entered are:")
    for city in cities:
        print(city)
# Run the program
city_names()
