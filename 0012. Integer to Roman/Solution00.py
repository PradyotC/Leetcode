/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.85 %
    Runtime : 71 ms
    Memory Usage : 13.9 MB
    Testcase : 3999 / 3999 passed
    Ranking : 
        Your runtime beats 59.91 % of python3 submissions.
        Your memory usage beats 79.96 % of python3 submissions.
}
*/

class Solution:
    def intToRoman(self, num: int) -> str:
        dictt = {1:"I",
                 5:"V",
                 10:"X",
                 50:"L",
                 100:"C",
                 500:"D",
                 1000:"M"}
        i = 0
        l1 = sorted(dictt.keys(),reverse=True)
        ans = {k:0 for k in l1}
        val = num
        while val!=0 and i<len(dictt):
            if val>=l1[i]:
                if l1[i] in ans.keys():
                    ans[l1[i]]+=1
                else:
                    ans[l1[i]]=1
                val-=l1[i]
            else:
                i+=1
        a1 = ""
        for i in range(len(l1)-1,0,-1):
            if ans[l1[i]]==4:
                if ans[l1[i-1]]==0:
                    a1 = dictt[l1[i]]+dictt[l1[i-1]]+a1
                else:
                    a1 = dictt[l1[i]]+dictt[l1[i-2]]+a1
                    ans[l1[i-1]]-=1
            else:
                a1 = (dictt[l1[i]]*ans[l1[i]])+a1
        a1 = (dictt[l1[0]]*ans[l1[0]]) + a1
        return a1
        