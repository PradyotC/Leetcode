class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            add = []
            for j in range(n):
                add.append(matrix[n-j-1][i])
            matrix.append(add)
            # print(matrix)
        [matrix.pop(0) for i in range(n)]
                