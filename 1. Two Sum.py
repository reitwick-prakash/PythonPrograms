#leetcode
#1. Two Sum


nums = [3,3]
target=6

length=len(nums)

ans=[]
sum=0
for i in range(length):
    for j in range(i+1,length):
        sum=nums[i]+nums[j]
        if sum==target:
            ans.extend([i,j])
#            ans.append(j)
print(ans)
            
        
        
