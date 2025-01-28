"""
2658. Maximum Number of Fish in a Grid
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
- A land cell if grid[r][c] = 0, or
- A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

- Catch all the fish at cell (r, c), or
- Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish.
"""

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        queue = []
        visited = set()
        r_c_delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    visited.add((i, j))
                    count = grid[i][j]
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)
                        for row, col in r_c_delta:
                            r = x + row
                            c = y + col
                            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > 0 and (r, c) not in visited:
                                count += grid[r][c]
                                queue.append((r, c))
                                visited.add((r, c))
                    
                    if max_fish < count:
                        max_fish = count
        
        return max_fish
