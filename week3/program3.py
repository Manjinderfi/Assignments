# Program to check hemoglobin levels based on gender

# Ask the user for their biological gender and hemoglobin value
gender = input("Enter your biological gender (female/male): ").lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender entered. Please enter 'female' or 'male'.")
