"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        r_c_delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    queue = [(i, j)]
                    visited.add((i, j))
                    while queue:
                        x, y = queue.pop(0)
                        for row, col in r_c_delta:
                            r = x + row
                            c = y + col
                            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in visited:
                                queue.append((r, c))
                                visited.add((r, c))
        
        return islands
