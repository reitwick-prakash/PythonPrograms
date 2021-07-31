#leetcode
#question - 4. Median of Two Sorted Arrays
#level=hard

import statistics

nums1 = [1,2]
nums2 = [3,4]

nums=nums1 + nums2
med=statistics.median(nums)

print(med)