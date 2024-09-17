def gallons_to_liters(gallons):
    """Converts gallons to liters."""
    return gallons * 3.78541

def main():
    """Asks the user for a volume in gallons and converts it to liters until a negative value is entered."""
    while True:
        try:
            gallons = float(input("Enter volume in gallons (or a negative number to quit): "))
            if gallons < 0:
                print("Negative value entered. Exiting.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
