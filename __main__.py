
import gausswrap as spall

def main():

    print("""Choose what you want to test: 
    1. spawn code on each run on native environment
    2. spawn code on each run in a container
    3. spawn onnce and ping after on native environment 
    4. spawn onnce and ping after on container environment 
    % note any other input will exit """)

    try: 
        x=int(input())
        if (1<=x<=4): 
            selector(x)
        else: 
            raise Exception('out of range')
    except Exception as e: 
        print (e)
    
def selector(x): 
    if(x==1):
        spall.run_local();
    elif(x==2): 
        spall.run_container();
    elif(x==3): 
        spall.run_multilocal();
    elif(x==4):
        spall.run_multicontainer();
    else:
        print("shit")

if __name__ == "__main__":
    main()

