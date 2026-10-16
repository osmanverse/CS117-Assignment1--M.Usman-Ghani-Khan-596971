#this program ask the user how many resistors are connected in series. Then uses a loop to read the value
# of each resistor and print the total series resistance (R_total = R1 + R2 + ...).
num_resistors = int(input("Enter the number of resistors in series: "))
total_resistance = 0
for i in range(1, num_resistors + 1):
    resistor_value = float(input(f"Enter R{i} : "))
    total_resistance += resistor_value
print(f"\nTotal Series Resistance: {total_resistance} ohms")