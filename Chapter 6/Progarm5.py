def remove_odd_numbers(numbers):
    """
    Takes a list of integers and returns a new list with only the even numbers.
    """
    # Create an empty list to store the even numbers
    even_numbers = []

    # Loop through each number in the original list
    for number in numbers:
        # Check if the number is even
        if number % 2 == 0:
            # Add the even number to the new list
            even_numbers.append(number)

    # Return the list with even numbers
    return even_numbers


def main():
    """
    Creates a list of integers, removes the odd numbers, and prints both the original and the new list.
    """
    # Define a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to remove odd numbers
    even_list = remove_odd_numbers(original_list)

    # Print the original list
    print("Original list:", original_list)

    # Print the new list with only even numbers
    print("List with even numbers only:", even_list)


# This line ensures that the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
