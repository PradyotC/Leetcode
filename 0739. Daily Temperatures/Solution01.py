/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 67.43 %
    Runtime : 1647 ms
    Memory Usage : 25.5 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 57.33 % of python3 submissions.
        Your memory usage beats 22.47 % of python3 submissions.
}
*/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures+=[0]
        l = len(temperatures)
        ret = [0 for i in range(l)]
        i = 0
        stack = []
        while i<l-1:
            if not stack or stack==[]:
                stack.extend([(i,temperatures[i])])
                i+=1
            idx,temp = stack[-1]
            # print(stack,idx,i)
            while temperatures[i]<=temp:
                stack.extend([(i,temperatures[i])])
                idx,temp = stack[-1]
                # print(stack,idx,i)
                i+=1
                if i==l: break
            else:
                ret[idx] = i-idx
                stack.pop()
            # print(ret)
        return ret[:-1]