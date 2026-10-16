#this program takes the voltage V (in volts) and resistance R (in ohms) from the user and calculate the current
#I = V / R. If the current is more than 2 A, it prints "Fuse will blow"; otherwise it prints "Circuit is safe".
#If R is zero or negative, it prints "Invalid resistance" instead.

voltage = int(input('Enter the Voltage in volts = '))
resistance = int(input('Enter the Resistance in ohms = '))
Current = float(voltage/resistance)
print(f"{Current} A")
if Current > 2 :
    print("Fuse will blow")
elif resistance <= 0:
    print("Invalid Resistance.")
else:
    print("Circuit is safe.")