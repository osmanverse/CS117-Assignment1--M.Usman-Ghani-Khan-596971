#Write two functions: ohms_current(v, r) that returns the current I = V / R, and power_dissipated(i, r) that returns the power P = I² × R. Test them for V = 12 V and R = 6
def ohms_current(v, r):
    return v / r
def power_dissipated(i, r):
    return (i ** 2) * r
voltage = 12
resistance = 6
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
print(f"Current = {current:.1f} A")
print(f"Power = {power:.1f} W")