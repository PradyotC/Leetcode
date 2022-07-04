/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 74.46 %
    Runtime : 224 ms
    Memory Usage : 14.4 MB
    Testcase : 76 / 76 passed
    Ranking : 
        Your runtime beats 59.57 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        out = 0
        while truckSize and boxTypes:
            a = boxTypes.pop(0)
            if a[0]>truckSize: 
                out+=truckSize*a[1]
                break
            else:
                out+=a[0]*a[1]
                truckSize-=a[0]
        return out
        