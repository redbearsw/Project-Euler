nums = [3,5]
total = 0
for num in nums:
    for i in range (0,1000):
        multiple = num*i
        if multiple < 1000 and multiple%15!=0:
            total += multiple
        elif multiple < 1000 and multiple%15==0:
            total += (multiple/2.0)
            
        
        
print total
            
     
