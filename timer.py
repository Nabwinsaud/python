#lets built timer count down

import time

def count(t):
    while t:
        mins,secs=divmod(t,60) #divmod is built in python function
        timer='{:02d}:{:02d} '.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t-=1 #decrement time

    print('Time stopped to 0') 

t=int(input('Enter count down time:')) 

count(t)
#thanks for viewing////.............
