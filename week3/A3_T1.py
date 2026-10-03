print("program starting.")
print("insert two integers.")
int_one = int(input("Insert first integer: "))
int_two = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if int_one > int_two:
    print("First integer is greater.")
elif int_one < int_two:
    print("Second integer is greater.")
else:
    print("Integers are the same.")

print()

print("Adding integers together")
print(int_one, "+", int_two, "=", int_one + int_two)

print()

print("Checking the parity of the sum...")
if (int_one + int_two) % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")    