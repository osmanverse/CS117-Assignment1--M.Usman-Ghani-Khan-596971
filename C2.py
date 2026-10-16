# Function to calculate the equivalent resistance in parallel
def parallel_resistance(resistors):
    sum_inverse = 0
    for r in resistors:
        # Add the reciprocal (1 / r) of each resistor
        sum_inverse += 1 / r
    r_eq = 1 / sum_inverse
    return round(r_eq, 2)
test1 = [10, 10]
test2 = [100, 200, 300]

print(f"parallel_resistance({test1}) -> {parallel_resistance(test1)}")
print(f"parallel_resistance({test2}) -> {parallel_resistance(test2)}")