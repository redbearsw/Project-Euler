# note that odd * odd == odd
# so, 3n + 1 is always even and therefore the next step is to divide by 2

def collatzLength(num):
    count = 0
    while num > 1:
        if (num % 2 == 0):
            num /= 2
            count += 1
        else:
            num = (3 * num + 1)/2
            count += 2
    return count + 1

def maxCollatz():
    max = 0
    maxStart = 0
    for i in range(1000000):
        col = collatzLength(i)
        print(i, ":",  col)
        if (col > max):
            max = col
            maxStart = i
    return maxStart

def main():
    length = maxCollatz()
    print(length)

if __name__ == "__main__":
    main()


