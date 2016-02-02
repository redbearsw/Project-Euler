fact = [1]
a = 2

def factors(x):
    for i in range (2, x+1):
        if x%i == 0 and x/i != 1:
            fact.append(i)
        else:
            print "%d is not a factor of %d" %(i, x)
    print fact

factors(36)

primes = []

#want to make this function take in a list of factors
def primefactors(x):
    for p in fact:
        for i in range (2,x+1):
            if p%i == 0 and p/i != 1:
                primefactors(p/i)
                print "checking %d now" %p/i
            else:
                primes.append(p)
                print "appending %d" %p
    print primes

primefactors(36)
