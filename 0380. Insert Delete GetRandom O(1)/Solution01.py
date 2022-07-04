/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 51.59 %
    Runtime : 488 ms
    Memory Usage : 61.5 MB
    Testcase : 19 / 19 passed
    Ranking : 
        Your runtime beats 80.78 % of python3 submissions.
        Your memory usage beats 21.21 % of python3 submissions.
}
*/

from random import choice
class RandomizedSet:

    def __init__(self):
        self.dictt = {}
        self.listt = []

    def insert(self, val: int) -> bool:
        if val in self.dictt: return False
        self.dictt[val] = len(self.listt)
        self.listt.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dictt: return False
        idx = self.dictt[val]
        del self.dictt[val]
        if self.listt[idx] == self.listt[-1]: 
            self.listt.pop()
            return True
        self.listt[idx] = self.listt[-1]
        self.listt.pop()
        self.dictt[self.listt[idx]] = idx
        return True

    def getRandom(self) -> int:
        return choice(self.listt)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()