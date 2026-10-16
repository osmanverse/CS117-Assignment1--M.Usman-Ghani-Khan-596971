#In this program we are testing a batch of manufactured 100-ohm resistors to bin them by tolerance. Write a program with a while loop that continuously
#asks the user to input a measured resistance value. The loop should stop when the user enters 0.
# Sort the inputs into three running counts:
#• 1% tolerance (99.0 to 101.0 ohms)
#• 5% tolerance (95.0 to 105.0 ohms, excluding those that qualify for 1%)
#• Reject (outside 95.0 to 105.0 ohms) Print the final count of resistors in each bin once the loop terminates.

count_1_percent = 0
count_5_percent = 0
count_reject = 0

print("--- Resistor Tolerance Sorting System ---")
print("Enter measured resistance values (Type 0 to finish):\n")

while True:
    resistance = float(input("Enter measured resistance (ohms): "))
    if resistance == 0:
        break
    if 99.0 <= resistance <= 101.0:
        count_1_percent += 1
    elif 95.0 <= resistance <= 105.0:
        count_5_percent += 1
    else:
        count_reject += 1
print("\nFINAL BIN COUNTS")
print(f"1% Tolerance Bin (99.0 - 101.0 Ω): {count_1_percent}")
print(f"5% Tolerance Bin (95.0 - 105.0 Ω): {count_5_percent}")
print(f"Reject Bin (Outside 95.0 - 105.0 Ω): {count_reject}")