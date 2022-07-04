/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.43 %
    Runtime : 392 ms
    Memory Usage : 14.9 MB
    Testcase : 103 / 103 passed
    Ranking : 
        Your runtime beats 27.89 % of python3 submissions.
        Your memory usage beats 16.74 % of python3 submissions.
}
*/

class Solution:
    def minDeletions(self, s: str) -> int:
        dictt = {}
        for i in s:
            dictt[i] = dictt.get(i,0)+1
        # print(dictt)
        revdictt = {}
        maxx = max(dictt.values())
        for i in set(dictt.values()):
            for j in dictt.keys():
                if dictt[j]==i:
                    revdictt[i] = revdictt.get(i,[])+[j]
        count = 0
        for i in range(maxx,0,-1):
            if i not in revdictt: continue
            while len(revdictt[i])!=1:
                if i-1 not in revdictt: revdictt[i-1]=[]
                revdictt[i-1].append(revdictt[i].pop())
                count+=1
        return count