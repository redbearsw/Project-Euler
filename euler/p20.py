# need to do array-based factorial
# remainder = 0
# list with 1 in it
# list[len] * i
# reset to answer % 10
# add remainder
# all while idx > 0
# add final remainder

def myMult(list, num):
    remainder = 0
    # multiply and carry over
    for i in range(len(list)):
        lastIdx = len(list) - 1
        dig = list[lastIdx - i]
        dig *= num
        dig += remainder
        list[lastIdx - i] = dig % 10
        remainder = dig / 10

    # dealing with final remainder
    while (remainder > 9):
        list.insert(0, remainder % 10)
        remainder /= 10

    list.insert(0, remainder)

    return list

def myFact(num):
    answer = [1]
    for i in range(1, num + 1):
        answer = myMult(answer, i)
    return answer

def sumList(list):
    sum = 0
    for dig in list:
        sum += dig
    return sum

def main():
    answer = myFact(100)
    sum = sumList(answer)
    print(sum)

if __name__ == "__main__":
    main()


