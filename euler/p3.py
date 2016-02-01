fact = [1]
a = 2

def primefactors(x):
    while a < 100:
        if x%a == 0 and x/a != 1:
            primefactors(x/a)
        else:
            fact.append(x)
            a += 1
            primefactors(x)



print fact

primefactors(10)


def primefactors():
    print fact.pop()
    while len(fact) != 0:
        for i in range (1,1000):
            if fact.pop()%i == 0:
                print fact.pop()/i
            else:
                print fact.pop()
