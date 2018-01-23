def find_sum(base, exp):
    num = long(base ** exp)
    sum = num % 10
    while (num > 0):
        sum += num / 10 % 10
        num /= 10
    print sum

find_sum(2, 15)
find_sum(2, 1000)

