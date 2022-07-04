/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 51.59 %
    Runtime : 1093 ms
    Memory Usage : 61.2 MB
    Testcase : 19 / 19 passed
    Ranking : 
        Your runtime beats 10.43 % of python3 submissions.
        Your memory usage beats 75.86 % of python3 submissions.
}
*/

from random import sample
class RandomizedSet:

    def __init__(self):
        self.sett = set()

    def insert(self, val: int) -> bool:
        if val in self.sett: return False
        self.sett.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.sett: return False
        self.sett.remove(val)
        return True

    def getRandom(self) -> int:
        return sample(self.sett, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()