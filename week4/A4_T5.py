print("Program starting.")
print()
start = int(input ("Insert starting point:"))
stop = int(input ("Insert stopping point:"))
inspection = int(input ("Insert inspection point:"))
print()
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
elif inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
else:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        print(i, end=" " if i < inspection - 1 else "\n")

    print("Second loop - inspection with continue:")
    numbers = []
    for i in range(start, stop):
        if i == inspection:
            continue
        numbers.append(str(i))
    print(" ".join(numbers))

print()
print("Program ending.")