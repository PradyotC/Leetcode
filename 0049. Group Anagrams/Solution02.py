/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.80 %
    Runtime : 224 ms
    Memory Usage : 22.1 MB
    Testcase : 117 / 117 passed
    Ranking : 
        Your runtime beats 13.23 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]: return [[""]]
        def retdict(r):
            rdict = {}
            for i in r:
                rdict[i]=rdict.get(i, 0)+1
            return rdict       
        ansdict = {}
        while strs:
            a = strs.pop()
            k = tuple(sorted(retdict(a).items()))
            if k in ansdict: ansdict[k]+=[a]
            else: ansdict[k]=[a]
        return ansdict.values()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
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
                elem = []
                for i in element:
                    del ans[i]
                    strs,e = sameoccur(strs,i)
                    elem+=e
            ansset.append(elem)
        return ansset
    '''