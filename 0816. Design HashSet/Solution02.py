/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 66.13 %
    Runtime : 301 ms
    Memory Usage : 18.8 MB
    Testcase : 33 / 33 passed
    Ranking : 
        Your runtime beats 53.90 % of python3 submissions.
        Your memory usage beats 72.15 % of python3 submissions.
}
*/

class MyHashSet:

    def __init__(self):
        self.mod = 97
        self.l = [None for i in range(self.mod)]

    def add(self, key: int) -> None:
        hashh = key%self.mod
        if not self.l[hashh]: self.l[hashh]=[key]
        elif key not in self.l[hashh]: self.l[hashh].append(key)

    def remove(self, key: int) -> None:
        hashh = key%self.mod
        if self.l[hashh] and key in self.l[hashh]: 
            self.l[hashh].remove(key)
            if not self.l[hashh]: self.l[hashh]=None

    def contains(self, key: int) -> bool:
        hashh = key%self.mod
        return True if self.l[hashh] and key in self.l[hashh] else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)