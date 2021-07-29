#leetcode
#121. Best Time to Buy and Sell Stock
#easy

prices = [7,6,4,3,1]

minVal = prices[0]
profit = 0
for i in range(1,len(prices)):
    if(prices[i]<minVal):
        minVal = prices[i]
    else:
        profit = max(profit, prices[i] - minVal)

print(profit)