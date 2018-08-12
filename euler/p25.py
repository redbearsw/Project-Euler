def num_digits(num):
    i = 0
    while num >= 1:
        i += 1
        num /= 10
    return i

def thousand_fib():
    prev = 1
    curr = 1
    idx = 2
    while (num_digits(curr) < 1000):
        print("just checked", prev, curr)
        next_num = prev + curr
        prev = curr
        curr = next_num
        idx += 1

    return idx

def main():
    answer = thousand_fib()
    print("\n answer: %d" % answer)


main()
