def binary_to_decimal(binary):
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        return None
while True:
    binary_input = input("Enter a binary number: ")

    if all(char in '01' for char in binary_input):
        break
    else:
        print("Invalid input.")

decimal_result = binary_to_decimal(binary_input)

if decimal_result is not None:
    print(f"The decimal equivalent of {binary_input} is: {decimal_result}")
else:
    print("Invalid binary number.")