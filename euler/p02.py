def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
print fib(8)

fibs = []

def listfibs():
    for i in range (1, 34):
        if fib(i) % 2 == 0:    
            fibs.append(fib(i))
        else:
            fibs == fibs
    print fibs
     
listfibs()

b = sum(fibs)

print b
        
       
        





        
     
        
        




    
   
    
    

    
    
    
    
    
    
