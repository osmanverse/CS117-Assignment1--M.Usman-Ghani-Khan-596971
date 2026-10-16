# This program takes three resistor values from the user and display the smallest and the largest of them.
# it uses only if/ elif /else (no min() or max()).

r1 = int(input("Enter R1 : "))
r2 = int(input("Enter R2 : "))
r3 = int(input("Enter R3 : "))

if r1>r2 and r1>r3 and r2>r3:
    print(f"Smallest = {r3} ohm")
    print(f"Largest = {r1} ohm")
elif r2>r3 and r2>r1 and r3>r1:
    print(f"Smallest = {r1} ohm")
    print(f"Largest = {r2} ohm")
elif r3>r1 and r3>r2 and r1>r2 :
    print(f"Smallest = {r2} ohm")
    print(f"Largest = {r3} ohm")
else:
    print('All are equal')