#leetcode
#1471. The k Strongest Values in an Array


arr = [6,7,11,7,6,8]
k=5

n=len(arr)
med=int((n-1)/2)
arr.sort()
#print(med)

arr_strong=[]
for i in arr:
    strongness=abs(i-arr[med])
    arr_strong.append([strongness,i])    
arr_strong.sort(reverse=True)
#print(arr_strong)

final=[]
for i,j in arr_strong:
#    print(j)
    if len(final)<k:
        final.append(j)

print(final)
    
    
        
