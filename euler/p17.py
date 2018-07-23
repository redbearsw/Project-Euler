ones = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
ten = 3
eleven = 6
twelve = 6
thir_to_nine = 4 + 4 + 3 + 3 + 5 + 4 + 4
thirteen_to_nineteen = thir_to_nine + (4 * 7)
twenty = 6
tens = ten + eleven + twelve + thirteen_to_nineteen + ((thir_to_nine + 14 + twenty) * 10) + (ones * 8) #ten to nineteen + 10 times (each prefix (thirty, forty, etc) + 2 per prefix + "twenty") + ones are suffixes 8 times
hundreds = (ones * 100) + ((tens + ones) * 9) + (10 * 900) # each ones is prefix to "hundred" 100 times + each number from 0 to 99 follows each of the 9 hundreds + "hundred and" has 10 letters * use it 900 times for numbers from 100 to 999

print hundreds + tens + ones + 11
