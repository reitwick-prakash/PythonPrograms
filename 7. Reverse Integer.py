#leetcode
#question - 7. Reverse Integer
#level=easy


x=5455

revs=0

if 2147483647>x>0: 
    while 2147483647>x>0:
        remainder=x%10
        revs=(revs*10)+remainder
        x=x//10
        
elif -2147483647<x<0:
    x=abs(x)
    while 2147483647>x>0:
        remainder=x%10
        revs=(revs*10)+remainder
        x=x//10
    revs=-revs

if revs>2147483647 or revs<-2147483647:
    print("0")
else:    
    print(revs)
