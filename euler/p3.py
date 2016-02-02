
fact=[1]
#makes a list of factors of x
def factors(x):
    for i in range (2, x+1):
        if x%i == 0 and x/i != 1:
            fact.append(i)
        else:
            return fact

factors(36)

print fact




#only keeps the prime factors of x
def prime(x):
    for i in range (2,x+1):
        if x%i == 0 and x/i != 1:
            prime(x/i)
        else:
            return x
#tests
prime(1)
prime(2)
prime(3)
prime(5)
prime(6)
prime(7)
prime(8)
prime(9)
prime(10)



primefactors = []
def primefactors():
    for i in fact:
        if prime(i):
            return i
        else:
            print "%d is not a primefactor" %i

primefactors()
