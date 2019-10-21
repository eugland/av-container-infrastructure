# Defining our function as seidel which takes 3 arguments 
# as A matrix, Solution and B matrix 
import sys 
import time 


# define constants




def seidel(x):
    a = [[4,1,2,1,1],[3,5,1,1,1],[1,1,3,1,1],[1,1,1,5,1], [1,1,1,1,9]] 
    b = [4,7,3,9,2] 
    
    # print('GOTO: ' + __name__ + '.sedial()') 
    # print(x)
    n = len(a)                    
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i]   
        x[j] = d / a[j][j]         
    return x     

def run(x, inita): 
    # print('GOTO: ' + __name__ + '.run()')
    calllength = time.time() - inita
    pre = time.time()

    #loop run for m times depending on m the error value 
    for i in range(0, 2500):             
        x = seidel(x) 
        #print each time the updated solution 
    length = time.time() - pre
    res = ",".join(map(str, x))
    with open('/home/eugene/devspace/container/logs.csv', 'a+') as the_file:
        the_file.write(str(length) + ','+ str(calllength) + ',' + ",".join(map(str, x)) + '\n')
    # print(length)      
    return(x)

if (__name__ == '__main__'):
    initx = [0.1,0.1,0.1,0.1,0.1]
    ind = sys.argv[2:7]
    initx = [float(x) for x in ind]
    xd = run (initx, float(sys.argv[1])) 
    print(xd)