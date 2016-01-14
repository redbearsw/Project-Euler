fact = []

def factors(x):
    for i in range (1, 100):
        if x%i == 0:
            fact.append(i)
            print " %d is a factor" %i
        
       
factors(13195)

print fact

def primefactors():
    print fact.pop()
    while len(fact) != 0:    
        for i in range (1,1000): 
            if fact.pop()%i ==0:
                print fact.pop()/i
            else:
                print fact.pop()
            
primefactors()
       

    
    
    


    
    
