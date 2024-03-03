def decimal_to_binary(decimal_number):
    binary_representation = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_representation = str(remainder) + binary_representation
        decimal_number //= 2
    return binary_representation

def decimal_to_hexadecimal(decimal_number):
    hexadecimal_representation = ""
    hex_digits = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_representation = hex_digits[remainder] + hexadecimal_representation
        decimal_number //= 16
    return hexadecimal_representation


decimal_number = int(input("Enter a decimal number: "))

binary = decimal_to_binary(decimal_number)
hexadecimal = decimal_to_hexadecimal(decimal_number)

print(f"Binary representation: {binary}")
print(f"Hexadecimal representation: {hexadecimal}")

