#leetcode
#question - 9. Palindrome Number
#level=easy

x=-121
revs=0
org_num=x
while x>0:
    remainder=x%10
    revs=(revs*10)+remainder
    x=x//10

if org_num==revs:
    print("true")
    
else:
    print("false")