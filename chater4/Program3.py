def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to stop): ")

        if user_input == '':
            break

        try:
            number = float(user_input)  # Convert to a number
            numbers.append(number)      # Add the number to the list
        except ValueError:
            print("That's not a valid number. Please try again.")

    if numbers:
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        # If no numbers were entered, show a message
        print("No numbers were entered.")

find_min_max()
