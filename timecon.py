#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    list(s)
    n=len(s)
    print(n)
    a = [0,0]
    a[1]=s[n-1]
    a[0]=s[n-2]
    b = ''.join(a)
    print(b)
    if(b=="AM"):
        t=[0,0]
        t[0]=s[0]
        t[1]=s[1]
        tt = ''.join(t)
        print(tt)
        if(tt=='12'):
            hh='00'
        elif(int(tt)>12):
            sys.exit()
        elif(int(tt)<0):
            sys.exit()
        else:
            hh=tt
       # hh=hr[0]
        print(hh)
    else:
        t=[0,0]
        t[0]=s[0]
        t[1]=s[1]
        tt = ''.join(t)
        print(tt)
        if(tt=='12'):
            hh=12
        elif(int(tt)>12):
            sys.exit()
        elif(int(tt)<0):
            sys.exit()
        else:
            hh=int(tt)+12
        print(hh)
    j=0
    mit=[0,0,0,0,0,0]
    for i in range(2,8):
        mit[j] = s[i]
        j=j+1
    misec=''.join(mit)
    print(misec)

    ret= str(hh)+misec
    print(ret)

    return(ret)

    
        
        
        
        
   

if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)

    print(result + '\n')


