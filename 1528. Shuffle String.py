#leetcode
#question - 1528. Shuffle String
#level=Easy


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

x=zip(indices,s)
y=list(x)

    
z=sorted(y)
non_shuffled=[]
for i in range(0,len(z)):
    non_shuffled.append(z[i][1])

str1 = ''.join(non_shuffled)
print(str1)
