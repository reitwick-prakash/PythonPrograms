#leetcode
#question - 1512. Number of Good Pairs
#level=Easy


nums=[1,2,3]
pairs=[]

for i in range(0,len(nums)):
#    print(nums[i])
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            pairs.append([i,j])
print(len(pairs))