
print("Program starting.")
print()

x = int(input("Insert a positive integer: "))

a = 0
sequence = str(x)

while x != 1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = x * 3 + 1

    sequence += " -> " + str(x)
    a += 1

print(sequence)
print("Sequence had", a, "total steps.")

print()
print("Program ending.")