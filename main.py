from flask import Flask
import time 
import sys 

app = Flask(__name__)
# define constants
x = [0,0,0,0,0]    
a = [[4,1,2,1,1],[3,5,1,1,1],[1,1,3,1,1],[1,1,1,5,1], [1,1,1,1,9]] 
b = [4,7,3,9,2] 

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def home():
    return "Hello, World!"

def seidel(a, x ,b): 
    n = len(a)                    
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i]   
        x[j] = d / a[j][j]         
    return x     

@app.route("/run/<passage>/<call>")
def runner(passage, call): 

    # running loop
    xcall = float(call)
    pre = time.time()
    calllength = pre-xcall;
    # print(raw)    
    raw = passage.split(',')            
    x = [ float(element) for element in raw]
    # print(x) 
    
    #loop run for m times depending on m the error value 
    for i in range(0, 2500):             
        x = seidel(a, x, b) 
        #print each time the updated solution 
    output = [ str(element) for element in x]  
    length = time.time() - pre
    with open('/home/eugene/devspace/container/logs-naive.csv', 'a+') as the_file:
        the_file.write(str(length) + ','+ str(calllength) + ',' + ",".join(map(str, x)) + '\n')
    # print(length)      
    return(','.join(output))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
