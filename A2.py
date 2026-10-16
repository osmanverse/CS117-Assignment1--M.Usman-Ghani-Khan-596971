#This program takes a current value from the user. If it is positive, it prints "Current flows from A to B". If it is
#negative, it prints "Current flows from B to A". If it is zero, it prints "No current flows".

current = int(input("Enter the value of current= "))
if current >0:
    print('Current flows from A to B.')
elif current <0:
    print('Current flows from B to A.')
else:
    print("No Current flows.")