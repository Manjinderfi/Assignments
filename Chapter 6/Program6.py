import math


def calculate_unit_price(diameter_cm, price_euros):
    diameter_m = diameter_cm / 100.0
    radius_m = diameter_m / 2
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price_euros / area_m2
    return unit_price


def main():
    diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))
    diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


if __name__ == "__main__":
    main()
