
SIZE_LIMIT = 42

length = float(input("Enter the length of the zander in centimeters: "))

if length >= SIZE_LIMIT:
    print("The zander meets the size limit.")
else:
    difference = SIZE_LIMIT - length
    print(f"The zander does not meet the size limit. Please release the fish back into the lake.")
    print(f"The zander is {difference} centimeters below the size limit.")
