#Write a function star_to_delta(ra, rb, rc) that takes three resistance values from a Star (Y) 
# network and converts them to the equivalent Delta (Δ) network. The function must calculate the numerator factor first to avoid redundant calculations


def star_to_delta(ra, rb, rc):
    thenumerator = ra * rb + rb * rc + rc * ra

    rab = thenumerator / rc
    rbc = thenumerator / ra
    rca = thenumerator / rb

    return (round(rab, 2), round(rbc, 2), round(rca, 2))


result = star_to_delta(10, 20, 30)
print(result)
