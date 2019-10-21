# Defining our function as seidel which takes 3 arguments 
# as A matrix, Solution and B matrix 
import sys 
import time 

# define constants
x = [0,0,0,0,0]    
a = [[4,1,2,1,1],[3,5,1,1,1],[1,1,3,1,1],[1,1,1,5,1], [1,1,1,1,9]] 
b = [4,7,3,9,2] 

def seidel(a, x ,b): 
    n = len(a)                    
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i]   
        x[j] = d / a[j][j]         
    return x     

def run(raw): 
    # running loop
    pre = time.time()   
    # print(raw)    
    raw = raw.split(',')            
    x = [ float(element) for element in raw]
    # print(x) 
    
    #loop run for m times depending on m the error value 
    for i in range(0, 2500):             
        x = seidel(a, x, b) 
        #print each time the updated solution 
    output = [ str(element) for element in x]  
    length = time.time() - pre
    with open('/home/eugene/devspace/container/logs', 'a+') as the_file:
        the_file.write('TIME:' + str(length) + ' RESULT:' + str(output)+ '\n')
    # print(length)      
    return(','.join(output))
