ones = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
ten_to_twelve = 3 + 6 + 6
thirteen_to_nineteen = 4 + 4 + 3 + 3 + 5 + 5 + 4 + (4 * 7)
tens = ten_to_twelve + thirteen_to_nineteen + (4 * 60) + (3 * 50) + 70 + (8 * ones)
hundreds = (3 * 1000) + (2 * 1100) + (3 * 1200) + (9 * (ones + tens)) + (3 * 891)

print hundreds + tens + ones + 11
