"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_size = len(mat)
        col_size = len(mat[0])
        queue = []

        for i in range(row_size):
            for j in range(col_size):
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = "#"
        
        while len(queue) > 0:
            row, col = queue.pop(0)
            r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in r_c_delta:
                r = row + dr
                c = col + dc
                if (0 <= r < row_size) and (0 <= c < col_size) and (mat[r][c] == "#"):
                    mat[r][c] = mat[row][col] + 1
                    queue.append([r, c])
        
        return mat
