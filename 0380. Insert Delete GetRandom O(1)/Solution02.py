/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 51.59 %
    Runtime : 1138 ms
    Memory Usage : 61.5 MB
    Testcase : 19 / 19 passed
    Ranking : 
        Your runtime beats 9.04 % of python3 submissions.
        Your memory usage beats 21.21 % of python3 submissions.
}
*/

import random
class RandomizedSet:

    def __init__(self):
        self.sett = set()
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.sett: return False
        self.sett.add(val)
        self.len+=1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.sett: return False
        self.sett.remove(val)
        self.len-=1
        return True

    def getRandom(self) -> int:
        return list(self.sett)[random.randint(0,self.len-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()