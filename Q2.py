def binary_to_decimal(binary):
    try:
        d = int(binary, 2)
        return d
    except ValueError:
        return None
while True:
    binary_number = input("Enter a binary number: ")

    if all(char in '01' for char in binary_number):
        break
    else:
        print("Invalid input.")

d_result = binary_to_decimal(binary_number)

if d_result is not None:
    print(f"The decimal equivalent of {binary_number} is: {d_result}")
else:
    print("Invalid binary number.")
