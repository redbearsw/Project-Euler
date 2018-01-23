def find_largest_prime(i):
    base = i
    factor = base/2;
    while factor > 1:
        if (base % factor != 0):
            print factor, "isn't a factor"
            factor -= 1
        else:
            base = factor
            factor = factor / 2
            print "new base:", base
    return base

print "13195:", find_largest_prime(13195)
print "4294967296:", find_largest_prime(4294967296)
print "problem answer:", find_largest_prime(600851475143)

