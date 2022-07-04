/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.64 %
    Runtime : 249 ms
    Memory Usage : 14.3 MB
    Testcase : 136 / 136 passed
    Ranking : 
        Your runtime beats 57.81 % of python3 submissions.
        Your memory usage beats 87.76 % of python3 submissions.
}
*/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sett = tuple(set(list1).intersection(set(list2)))
        if len(sett)==1:
            return sett
        ans = {}
        for i in range(len(list1)):
            if list1[i] in sett:
                ans[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in sett:
                ans[list2[i]]+=i
        min_value = min(ans.values())
        return [k for k,v in ans.items() if v==min_value]
        