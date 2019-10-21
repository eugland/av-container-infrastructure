import time 
import subprocess 
import requests
import main

import gausse as m

CONST_TIME_TAKING_TIME  = 0

TRIAL = 100

def run_local():
    """ testing how long time get is: 
    take time 3 times then divide by 3
    
    """
    # print('GOTO: ' + __name__ + 'run_local()')
    pre = time.time()
    whentime = time.time()
    CONST_TIME_TAKING_TIME = time.time() - pre
    inita = [0.01,0.01,0.01,0.01,0.01]

    for i in range (0,TRIAL): 
        m.run(inita,time.time())
    print(time.time()-pre)

   
def run_container():
    """ testing how long time get is: 
    take time 3 times then divide by 3
    
    """
    # print('GOTO: ' + __name__ + 'run_container()')
    pre = time.time()
    whentime = time.time()
    CONST_TIME_TAKING_TIME = time.time() - pre
    inita = [0.01,0.01,0.01,0.01,0.01]
    
    print (bash('docker build -t gausse:latest . -f Dockerfile_singlerun')[0])
    for i in range (0,TRIAL): 
        output = bash('docker run -v /home/eugene/devspace/container/log:/home/eugene/devspace/container/ gausse '+str(time.time())+' '+'0 0 0 0 0' )
        print(output)
    print(time.time()-pre)

def run_multilocal(): 
    """ testing how long time get is: 
    take time 3 times then divide by 3
    
    """
    # print('GOTO: ' + __name__ + 'run_container()')
    pre = time.time()
    whentime = time.time()
    CONST_TIME_TAKING_TIME = time.time() - pre
    inita = [0.01,0.01,0.01,0.01,0.01]
    process = subprocess.Popen("python3 main.py".split())
    time.sleep(2.4)
    inita = "0,0,0,0,0"
    pre = time.time()
    for i in range (0,TRIAL): 
        r = requests.get('http://localhost:5000/run/'+inita+'/'+str(time.time()));
        inita = r.text;
    subprocess.call("fuser -k 5000/tcp".split());
    print(time.time()-pre)


def run_multicontainer():
    """ testing how long time get is: 
    take time 3 times then divide by 3
    
    """
    # print('GOTO: ' + __name__ + 'run_container()')
    pre = time.time()
    whentime = time.time()
    CONST_TIME_TAKING_TIME = time.time() - pre
    inita = [0.01,0.01,0.01,0.01,0.01]
    # output = bash('docker build -t gausse-online:latest . -f Dockerfile_multirun')
    # output = bash('pwd')
    # print(output)
   # subprocess.Popen('docker run -v /home/eugene/devspace/container/log:/home/eugene/devspace/container  gausse-online:latest' )

    time.sleep(2)
    inita = "0,0,0,0,0"
    output = [str(i) for i in inita]
    pre = time.time()
    for i in range (0,TRIAL): 
        r = requests.get('http://localhost:5000/run/'+inita+'/'+str(time.time()));
        inita = r.text;
    subprocess.call("fuser -k 5000/tcp".split());
    print(time.time()-pre)

def bash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

