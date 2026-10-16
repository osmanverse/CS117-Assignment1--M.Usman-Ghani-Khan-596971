# this program will find and print: (a) how many readings are above 3.2 V, 
# (b) the highest reading, (c) the lowest reading, (d) the average reading.
# Given tuple of voltage readings
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above_3_2_count = 0
total_sum = 0
count = 0

highest = readings[0]
lowest = readings[0]

for val in readings:
    if val > 3.2:
        above_3_2_count += 1
    if val > highest:
        highest = val
    if val < lowest:
        lowest = val

    total_sum += val
    count += 1

average = total_sum / count

print(f"Readings above 3.2 V: {above_3_2_count}")
print(f"Highest reading: {highest}")
print(f"Lowest reading: {lowest}")
print(f"Average reading: {average:.2f}")