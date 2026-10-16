#In this program, A battery management system records voltage readings every minute. Given a hardcoded list of readings such as voltages = [12.6,
#12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2], use a loop to find the longest consecutive streak of strictly decreasing voltage readings. Do not use built-in sorting or
#grouping functions. Print the length of the longest streak, as well as the starting and ending
#voltages of that specific sequence. Sample run: Longest continuous drop: 4 minutes Started at: 12.5 V Ended at: 11.9 V


voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
max_length = 1
current_length = 1
start_voltage = voltages[0]
end_voltage = voltages[0]
best_start = voltages[0]
best_end = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        if current_length == 1:
            start_voltage = voltages[i - 1]
            
        current_length += 1      # Increase streak length
        end_voltage = voltages[i] # Update the current ending voltage
        
    else:
        if current_length > max_length:
            max_length = current_length
            best_start = start_voltage
            best_end = end_voltage
        current_length = 1
        start_voltage = voltages[i]
        end_voltage = voltages[i]
if current_length > max_length:
    max_length = current_length
    best_start = start_voltage
    best_end = end_voltage

print(f"Longest continuous drop: {max_length} minutes")
print(f"Started at: {best_start} V")
print(f"Ended at: {best_end} V")