import sys

def decimal_to_hex(decimal_value):
    if not isinstance(decimal_value, int):
        raise TypeError("Input must be an integer") # Check Input value only integer numbers.

    if decimal_value<1:
        return print("Please provide Decimal value greater than 0") # Check Input value greater than 0 
     
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal  # Ensure concatenation works
        num //= 16
    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":

    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError: 
            print("Please provide a valid integer.")
    else:
         print("Error: No input provided. Please provide a decimal number.")
         sys.exit(1)
