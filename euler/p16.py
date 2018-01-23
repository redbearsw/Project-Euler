def find_sum(base, exp):
    num = long(base ** exp)
    #start with ones digit
    sum = num % 10
    #add each subsequent digit by dividing by ten and isolating
    while (num > 0):
        sum += num / 10 % 10
        num /= 10
    print sum

find_sum(2, 15)
find_sum(2, 1000)

