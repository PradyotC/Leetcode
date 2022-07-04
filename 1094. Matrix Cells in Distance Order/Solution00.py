/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.20 %
    Runtime : 309 ms
    Memory Usage : 15.9 MB
    Testcase : 66 / 66 passed
    Ranking : 
        Your runtime beats 25.05 % of python3 submissions.
        Your memory usage beats 73.26 % of python3 submissions.
}
*/

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def sorter(item): return abs(item[0]-rCenter)+abs(item[1]-cCenter)
        return sorted([[i,j] for i in range(rows) for j in range(cols)],key=sorter)