import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)

three_digit_code_str = str(digit1) + str(digit2) + str(digit3)

digit4 = random.randint(1, 6)
digit5 = random.randint(1, 6)
digit6 = random.randint(1, 6)
digit7 = random.randint(1, 6)

four_digit_code_str = str(digit4) + str(digit5) + str(digit6) + str(digit7)

print(f"3-digit code: {three_digit_code_str}")
print(f"4-digit code: {four_digit_code_str}")
