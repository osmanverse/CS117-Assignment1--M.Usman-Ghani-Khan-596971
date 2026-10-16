# Create a dictionary mapping each color to its resistor digit
color_codes = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
user_input = input("Enter the first band color: ").lower()
result = color_codes.get(user_input, "Invalid colour")
print(result)