import math
# What is the largest n-digits pandigital prime?

# original idea:
# start with n = 9, and go down
# start with 987654321, then 987654312, keep permuting in order
# check if number is prime

# revised idea:
# run through numbers starting at 987654321
# check if it's a permutation, then check if it's prime

# function that takes in n and makes a list of pandigital permutations in descending
# lexographic order
# def permute(n):
#     permutations = []
#     currPerm = []

#     # holds digits still available, in descending order
#     availDig = []
#     for i in range(1, n):
#         availDig.append(n + 1 - i)

#     currPerm = []

# checks if a number is pandigital
def isPandigital(num):
    numString = str(num)
    length = len(numString)
    # list of digits still available
    usedDig = []
    for char in numString:
        if (char in usedDig):
            return False
        else:
            usedDig.append(char)

    if len(usedDig) == length:
        return True
    else:
        return False


# function that checks if a number is prime
def isPrime(num):
    i = 3
    while (i < math.sqrt(num)):
        if num % i == 0:
            return False
        i += 2
    return True



def main():
    i = 987654321
    while (i > 0):
        print(i)
        if isPandigital(i):
            if isPrime(i):
                print(i)
        i -= 2

main()




print(isPermutation(987654321))
print(isPermutation(98765))
