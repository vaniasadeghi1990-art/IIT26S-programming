print("Program starting.")
print("Estimate how many minutes you spent on programming...")

A1_T1= int(input("A1_T1: "))
A1_T2= int(input("A1_T2: "))
A1_T3= int(input("A1_T3: "))
A1_T4= int(input("A1_T4: "))
A1_T5= int(input("A1_T5: "))
A1_T6= int(input("A1_T6: "))
A1_T7= int(input("A1_T7: "))
total_time= A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7
round_average= total_time/7
round_average=round(round_average,2)
rounded_average= round(round_average)
print(f"In total you spent {total_time} minutes on programming.")
print(f"Average per task was {round_average:.2f} minutes and same rounded to the nearest integer {rounded_average} min.")


print ("Program ending.")