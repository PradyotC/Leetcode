/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 72.49 %
    Runtime : 577 ms
    Memory Usage : 14.3 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 18.93 % of python3 submissions.
        Your memory usage beats 99.67 % of python3 submissions.
}
*/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        l = len(people)
        ret = [None for i in range(l)]
        people.sort()
        while people:
            k = people.pop(0)
            count = k[1]+1
            for i in range(l):
                if ret[i] and ret[i][0]!=k[0]: continue
                count-=1
                if not count:
                    ret[i]=k
                    break
        return ret
                
                
        