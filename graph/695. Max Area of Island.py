"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        r_c_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j):
            area = 1
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                for row, col in r_c_delta:
                    r = x + row
                    c = y + col
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area
