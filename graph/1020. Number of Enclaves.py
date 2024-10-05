"""
1020. Number of Enclaves
https://leetcode.com/problems/number-of-enclaves/

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the 
grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        count = 0
        queue = []
        r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(row_size):
            for c in range(col_size):
                if grid[r][c] == 1:
                    if (r == 0 or c == 0 or r == row_size - 1 or c == col_size - 1):
                        grid[r][c] = "#"
                        queue.append([r, c])

        while queue:
            row, col = queue.pop(0)
            for dr, dc in r_c_delta:
                r = dr + row
                c = dc + col
                if (0 <= r < row_size) and (0 <= c < col_size) and grid[r][c] == 1:
                    grid[r][c] = "#"
                    queue.append([r, c])
        
        for r in range(row_size):
            for c in range(col_size):
                if grid[r][c] == 1:
                    count += 1

        return count
