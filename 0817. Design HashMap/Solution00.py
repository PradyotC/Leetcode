/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 65.22 %
    Runtime : 450 ms
    Memory Usage : 17.3 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 40.10 % of python3 submissions.
        Your memory usage beats 63.24 % of python3 submissions.
}
*/

class MyHashMap:

    def __init__(self):
        self.mod = 37
        self.l = [None for i in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        hashh = key%self.mod
        if not self.l[hashh]: self.l[hashh]=[key,str(value)]
        else:
            if key in self.l[hashh]:
                i = self.l[hashh].index(key)
                self.l[hashh][i+1]=str(value)
            else: self.l[hashh]+=[key,str(value)]

    def get(self, key: int) -> int:
        hashh = key%self.mod
        if not self.l[hashh]: return -1
        if not key in self.l[hashh]: return -1
        i = self.l[hashh].index(key)
        return int(self.l[hashh][i+1])

    def remove(self, key: int) -> None:
        hashh = key%self.mod
        if self.l[hashh] and key in self.l[hashh]: 
            i = self.l[hashh].index(key)
            self.l[hashh].pop(i)
            self.l[hashh].pop(i)            
            if not self.l[hashh]: self.l[hashh]=None
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)