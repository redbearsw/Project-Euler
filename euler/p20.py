# need to do array-based factorial

def factorial(num):
    prod = 1
    twos = 0
    fives = 0
    for i in range(1, num + 1):
        if (i % 10 != 0):
            if (i % 5 == 0):
                fives += 1
            elif (i % 2 == 0):
                twos += 1
            else:
                prod *= i
            print(i, ":", prod)


    if (twos > fives):
        print("twos:", twos)
        for i in range(twos - fives):
            prod *= 2
            print(prod)
    elif (twos < fives):
        for i in range(fives - twos):
            prod *= 5
            print(prod)
    return prod

def digSum(num):
    sum = 0
    while num > 9:
        sum += num % 10
        num / 10
    sum += num
    return sum

def main():
    fact = factorial(100)
    sum = digSum(fact)
    print(sum)

if __name__ == "__main__":
    main()


