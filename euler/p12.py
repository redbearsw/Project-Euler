#!/usr/bin/env python

from operator import mul
from functools import reduce
import math

# finds the nth triangle number
# def triangleNum(n):
#     sum = 0
#     i = 1
#     while i <= n:
#         sum += i
#         i += 1
#     return sum

# returns a list of all prime factors of the number in ascending order
# num is the number, and start is which factor to start checking from (usually called with 3)
def primeFactRec(num, start):
    factors = []
    
    # divide out 2 until number is no longer even
    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    if num < 3:
        return factors

    # store sqrt so calculation isn't repeated
    sqrt = math.sqrt(num)

    # check all odd numbers
    for i in range (start,num + 1, 2):

        # if get past sqrt and there are no factors, it's prime
        if i > sqrt + 1 and not factors:
            factors.append(num)
            break

        # append if a factor and call recursively on num / factor
        if num % i == 0:
            factors.append(i)
            factors = factors + primeFact(num // i, i)
            break
    return factors

#prime factorization with loops not recursion
def primeFact(num):
    factors = []
    
    # divide out 2 until number is no longer even
    while num % 2 == 0:
        factors.append(2)
        num = num // 2
        
    if num < 3:
        return factors


    # store sqrt so calculation isn't repeated
    sqrt = math.sqrt(num)

    # check all odd numbers
    i = 3
    while i < num + 1:


        # if get past sqrt and there are no factors, it's prime
        if i > sqrt + 1 and not factors:
            factors.append(num)
            return factors

        # append if a factor and update num
        elif num % i == 0:
            factors.append(i)
            num = num // i

        else:
            i += 2
        
    return factors

# finds how many divisors the number has via prime factorization
def numDivFromPrime(num):

    # start with a list of (ordered) prime factors of the given number
    factors = primeFact(num)

    # create list of powers of the prime factors
    # ex. if factors = [2, 2, 5, 5, 5], this will output [2, 3]
    powers = []
    power = 1
    for i in range(len(factors) - 1):
        if factors[i] != factors[i + 1]:
            powers.append(power)
            power = 1
        else:
            power += 1
    powers.append(power)

    # count combinations of powers of prime factors
    return reduce(mul, map(lambda x: x + 1, powers))

# stupid brute force way of finding number of divisors by checking every possibility
def numDivisors(num):
    numDiv = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            numDiv += 1
    return numDiv

# def checkTriNum(num):
#     newNum = math.sqrt(1 + 8 * num)
#     if (newNum == int(newNum)):
#         return True
#     else:
#         return False



def main():

    # Find the first triangle number with over 500 divisors
    triNum = 0
    i = 1
    while True:
        triNum += i
        i += 1
        nd = numDivFromPrime(triNum)
        print("num: " + str(triNum) + " numDivisors: " + str(nd))
        if (nd > 1000):
            return triNum

if __name__ == "__main__":
    main()
