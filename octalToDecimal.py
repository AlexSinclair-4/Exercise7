def octalToDecimal(octal):
    decimal = 0
    power = 0
    while octal > 0:
        decimal += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1
    return decimal

user_input = input("Enter an octal number: ")
if user_input.isnumeric() and all(c in '01234567' for c in user_input):
    octal = int(user_input)
    decimal = octalToDecimal(octal)
    print(f"Decimal equivalent: {decimal}")
else:
    print("Invalid octal number.")