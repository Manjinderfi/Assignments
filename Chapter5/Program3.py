def is_prime():
    number = int(input("Enter an integer: "))

    if number < 2:
        print(f"{number} is not a prime number.")
        return

    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return

    print(f"{number} is a prime number.")


is_prime()
