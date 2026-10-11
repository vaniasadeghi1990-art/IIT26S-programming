
print("Program starting.")
print()
print("Check multiplicative persistence.")

x = int(input("Insert an integer: "))
steps = 0

while x >= 10:
    digits = str(x)
    result = 1

    for digit in digits:
        result = result * int(digit)

    print(" * ".join(digits), "=", result)

    x = result
    steps = steps + 1

print("No more steps.")
print()
print("This program took", steps, "step(s)")
print()
print("Program ending.")