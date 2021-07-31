#leetcode
#question - 771. Jewels and Stones
#level=Easy

jewels = "z"
stones = "ZZZ"

occ=0
for i in jewels:
    for j in stones:
        if i==j:
            occ+=1
print(occ)