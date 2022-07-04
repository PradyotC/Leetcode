/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 32.69 %
    Runtime : 199 ms
    Memory Usage : 14.6 MB
    Testcase : 74 / 74 passed
    Ranking : 
        Your runtime beats 52.75 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def hasGroupsSizeX (self, deck: List[int]) -> bool:
        uniqueDeck = list(set(deck))
        deckList = dict.fromkeys(uniqueDeck,0)
        for i in range(len(deckList)):
                deckList[uniqueDeck[i]] = deck.count(uniqueDeck[i])
        freqList = list(deckList.values())
        val1 = self.gcdIter(freqList)
        if val1 > 1:
            return True
        else:
            return False
        
    def gcdIter (self, list1):
        a = list1[0]
        list1 = list1[1:]
        for i in range(len(list1)):
                b = list1[i]
                a = math.gcd(a,b)
        return a

