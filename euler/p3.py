fact = [1]
a = 2

def factors(x):
    for i in range (2, 100):
        if x%i == 0:
            fact.append(i)
        else:
            print "%d is not a factor of %d" %(i, x)
    print fact

factors(35)

primes = []

def primefactors(x):
    fact = [factors(x)]
    while len(fact) > 0:
        for i in range (1,1000):
            if fact.pop()%i == 0:
                primefactors(fact.pop()/i)
            else:
                primes.append(fact.pop())
    print primes

primefactors(35)
