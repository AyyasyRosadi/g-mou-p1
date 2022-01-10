lampu = 10
saklar = 4
nyala = 0 
nyala2 = []
for i in range(1,saklar+1):
    total = []
    total2 = 0
    for j in range(1,lampu+1):
        total.append(j)
    for k in range(1,lampu+1):
        if k%i==0:
            total2 = k
            if total2 in total:
                total[total2-1]= 0
            elif total2 not in total:
                total[total2-1]=total2
        print(total)
                
            
            
            
        


        
        
    
    
