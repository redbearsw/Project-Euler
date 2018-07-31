# find amicable numbers:
#   find proper divisors of all numbers under 10000
#   class holding num and sum of divisors
#   store all classes in list
#   for each number, check sum and sum's sum
#   if equal, add both to sum and remove from list

class Number:
    def __init__(self, num, sumDiv):
        self.num = num
        self.sumDiv = sumDiv

import math
# returns sum of proper divisors of given number
def findPropDiv(num):
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

def createNums(limit):
    listOfNums = []
    for i in range(1, limit):
        number = Number(i, findPropDiv(i))
        listOfNums.append(number)

    return listOfNums


def findIdxOfVal(list, val):
    i = 0
    for item in list:
        if item.num == val:
            return i
        i += 1
    return -1

def findAmicSum(listOfNums):
    # for each number, check sum against sum's sum
    # if equal, add both
    totalSum = 0
    for number in listOfNums:
        # find index of Number object corresponding to sum
        idx = findIdxOfVal(listOfNums, number.sumDiv)
        if number.num == int(listOfNums[idx].sumDiv) and not(number.num == listOfNums[idx].num):
            print("found one!")
            # add to total
            totalSum += number.num
            totalSum += listOfNums[idx].num
            listOfNums.pop(idx)
            print(totalSum)

    return totalSum

nums = createNums(10000)
sum = findAmicSum(nums)
print(sum)


# num1 = Number(220, findPropDiv(220))
# num2 = Number(284, findPropDiv(284))
# list = [num1, num2]
# print(findAmicSum(list))
