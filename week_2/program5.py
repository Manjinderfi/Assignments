LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

talents_in_grams = talents * TALENT_TO_POUNDS * POUND_TO_LOTS * LOT_TO_GRAMS

pounds_in_grams = pounds * POUND_TO_LOTS * LOT_TO_GRAMS

lots_in_grams = lots * LOT_TO_GRAMS

total_grams = talents_in_grams + pounds_in_grams + lots_in_grams

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"The weight in modern units is: {kilograms} kilograms and {grams:.2f} grams.")
