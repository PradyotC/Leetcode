/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 69.49 %
    Runtime : 109 ms
    Memory Usage : 14.4 MB
    Testcase : 68 / 68 passed
    Ranking : 
        Your runtime beats 40.83 % of python3 submissions.
        Your memory usage beats 84.74 % of python3 submissions.
}
*/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l = len(rooms)
        visited = [False for i in range(l)]
        q = [0]
        while q:
            k = q.pop(0)
            if visited[k]: continue
            visited[k]=True
            q+=rooms[k]
        bool1 = True
        [bool1:=bool1 and i for i in visited]
        return bool1
        
            