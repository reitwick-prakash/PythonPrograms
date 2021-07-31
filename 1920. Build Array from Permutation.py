#leetcode
#question - 1920. Build Array from Permutation
#level=Easy

nums= [0,2,1,5,3,4]

arr=[]
for i in range(0,len(nums)):
    p=nums[nums[i]]
    arr.append(p)
    
print(arr)