# In this program, A resistor has a fixed value of 10 ohm. Using a for loop, print the current through it for supply
# voltages from 1 V to 10 V in steps of 1 V.
resistance = 10
for voltage in range (1, 11):
    current = voltage/resistance
    print(f' V={voltage}, I={current}')

