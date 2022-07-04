/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.29 %
    Runtime : 1305 ms
    Memory Usage : 24.6 MB
    Testcase : 211 / 211 passed
    Ranking : 
        Your runtime beats 69.47 % of python3 submissions.
        Your memory usage beats 97.63 % of python3 submissions.
}
*/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = prices[0]
        max1 = prices[0]
        mini = 0
        maxi = 0
        opt = [0]
        for i in range(1,len(prices)):
            if prices[i]<min1:
                if i<=maxi:
                    min1 = prices[i]
                    mini = i
                else:
                    maxi = mini = i
                    max1 = min1 = prices[i]
                    opt.append(max(opt[i-1],max1-min1))
                    continue
            if prices[i]>max1:
                max1 = prices[i]
                maxi = i
            opt.append(max(opt[i-1],max1-min1))
        return opt[-1]
                