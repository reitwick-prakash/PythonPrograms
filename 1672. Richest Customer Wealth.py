#leetcode
#question - 1672. Richest Customer Wealth
#level=Easy


accounts =[[2,8,7],[7,1,3],[1,9,5]]

Sum=[]

for i in accounts:
    total=0
    for j in i:
        total+=j        
    Sum.append(total)
print(max(Sum))