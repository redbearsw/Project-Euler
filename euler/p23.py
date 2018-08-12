# find the sum of all pos integers which cannot be written as the sum of two abundant numbers
import math

# returns sum of all proper divisors of a number
def sumPropDiv(num):
    sumOfDiv = 1
    lim = math.sqrt(num)
    i = 2
    while i < lim:
        if num % i == 0:
            sumOfDiv += i
            # print("adding", i)
            sumOfDiv += num / i
            # print("adding", num / i)
        i += 1
    return sumOfDiv

# returns list of all abundant numbers under given limit
def listAbund(limit):
    abundNums = []
    for i in range(1, limit):
        if (sumPropDiv(i) > i):
            abundNums.append(i)
            print("appending", i)

    return abundNums

# returns list of all possible sums of abundant numbers
def listSumOfAbund(abundNums):
    sums = []
    i = 0
    length = len(abundNums)
    for i in range(length):
        for j in range(i, length):
            sums.append(abundNums[i] + abundNums[j])
            print("summing", i, j)
    return sums

# find sum of all numbers that can't be written as sum of two abundant numbers
def sumNonSums(abundNums, limit):
    print("summingNonSums")
    sum = 0
    for i in range(limit):
        if (not (i in abundNums)):
            sum += i
    return sum

def main():
    abundNums = listAbund(28124)
    possSums = listSumOfAbund(abundNums)
    nonAbundSum = sumNonSums(possSums, 28124)

    print(nonAbundSum)

main()
