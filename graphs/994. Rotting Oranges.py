"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        queue = []
        row_size = len(grid)
        col_size = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while len(queue) > 0:
            r, c, t = queue.pop(0)
            r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            minutes = max(minutes, t)

            for row, column in r_c_delta:
                x = r + row
                y = c + column
                if (0 <= x < row_size) and (0 <= y < col_size) and grid[x][y] != 2 and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append([x, y, t + 1])
                    fresh -= 1
                    
        if fresh > 0:
            return - 1

        return minutes
