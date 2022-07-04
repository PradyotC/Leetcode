/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.80 %
    Runtime : 6220 ms
    Memory Usage : 19.3 MB
    Testcase : 116 / 116 passed
    Ranking : 
        Your memory usage beats 30.65 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def retdict(r):
            rdict = {}
            for i in r:
                rdict[i]=rdict.get(i, 0)+1
            return rdict
        
        def sameoccur(lst,val):
            uni = []
            dup = []
            for i in strs:
                if i==val:
                    dup.append(val)
                else:
                    uni.append(i)
            return list(uni),list(dup)
                    
        ans = {}
        for i in strs:
            ans[i]=retdict(i)
        ansset = []
        while strs:
            elem = []
            if strs[0]=="":
                strs,elem = sameoccur(strs,"")
                del ans[""]
            else:
                val = ans[strs[0]]
                element = []
                for k,v in ans.items():
                    if v==val:
                        element.append(k)
                    # print(val,v,elem,strs)
                elem = []
                for i in element:
                    del ans[i]
                    strs,e = sameoccur(strs,i)
                    elem+=e
            ansset.append(elem)
        return ansset