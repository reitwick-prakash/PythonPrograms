#leetcode
#question - 13. Roman to Integer
#level=easy


s="XXIVIM"

add=0
roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

for i in range(0,len(s)-1):
    if roman[s[i]]<roman[s[i+1]]:
        add-=roman[s[i]]
    else:
        add+=roman[s[i]]
    
print(add+roman[s[-1]])
    
        