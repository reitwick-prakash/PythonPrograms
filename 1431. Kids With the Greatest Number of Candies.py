#leetcode
#question - 1431. Kids With the Greatest Number of Candies
#level=Easy

candies = [2,3,5,1,3]
extraCandies = 3
final=[]

for i in candies:
    check=i+extraCandies
    if check>=max(candies):
        final.append(True)
    else:
        final.append(False)

print(final)