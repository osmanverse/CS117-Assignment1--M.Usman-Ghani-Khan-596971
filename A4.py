# This program takes two bits A and B (each 0 or 1) from the user and print the output of the AND, OR and
#XOR gates. If either input is not 0 or 1, print "Bits must be 0 or 1".

input_a = input("Enter A : ")
input_b = input("Enter B : ")
if input_a not in ["0", "1"] or input_b not in ["0", "1"]:
    print("Bits must be 0 or 1")
else:
    A = int(input_a)
    B = int(input_b)

    AND = A & B  # AND: 1 only if both are 1
    OR = A | B   # OR: 1 if at least one is 1
    XOR = A ^ B  # XOR: 1 if inputs are different

    print(f"\n The Gate Outputs are")
    print(f"AND Output: {AND}")
    print(f"OR Output: {OR}")
    print(f"XOR Output: {XOR}")