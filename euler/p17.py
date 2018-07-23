# ones
ones = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

# tens
ten = 3
eleven = 6
twelve = 6
thir_to_nine = 4 + 4 + 3 + 3 + 5 + 4 + 4
thirteen_to_nineteen = thir_to_nine + (4 * 7)
twenty = 6
tens = ten + eleven + twelve + thirteen_to_nineteen + (((thir_to_nine - 1) + 14 + twenty) * 10) + (ones * 8) #ten to nineteen + 10 times (each prefix (thirty, forty, etc) adjusted because "fourteen" but "forty" + 2 per prefix + "twenty") + each ones digit is a suffix 8 times

# hundreds
hundreds = (ones * 100) + ((tens + ones) * 9) + (7 * 900) + (3 * (900 - 9)) # each ones is prefix to "hundred" 100 times + each number from 0 to 99 follows each of the 9 hundreds + "hundred" has 7 letters * use it 900 times for numbers from 100 to 999 + "and" has 3 letters * use it 900 - 9 times for numbers from 100 to 999 not including even hundreds

one_thousand = 11

print hundreds + tens + ones + one_thousand
