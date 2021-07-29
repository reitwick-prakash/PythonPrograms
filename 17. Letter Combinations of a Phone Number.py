#leetcode
#question - 17. Letter Combinations of a Phone Number
#level=Med

digits="23"

nums={"2":"abc","3":"def","4": "ghi","5": "jkl","6": "mno", "7": "pqrs", "8": "tuv","9": "wxyz"}

if len(digits)==0:
    result=[]
    
else:
    result=['']
    for i in digits:
        temp=[]
        for j in result:
#            print(j)
            for c in nums[i]:    
                temp.append(j+c)
        result=temp
print(result)