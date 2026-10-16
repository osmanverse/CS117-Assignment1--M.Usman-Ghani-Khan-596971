#This program is about the concept of Voltage Divider

def loaded_divider(vs, r1, r2, rl):
    unloaded = vs * r2 / (r1 + r2)

    req = (r2 * rl) / (r2 + rl)

    loaded = vs * req / (r1 + req)

    return (round(unloaded, 2), round(loaded, 2))


result = loaded_divider(12, 1000, 1000, 500)
print(result)
