"""
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        queue = []
        visited = set()
        r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    break
            if len(queue) > 0:
                break
        
        while len(queue):
            r, c = queue.pop(0)
            for row, col in r_c_delta:
                x = row + r
                y = col + c
                if (x, y) not in visited:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == 0:
                            perimeter += 1
                        else:
                            queue.append((x, y))
                            visited.add((x, y))
                    else:
                        perimeter += 1
        
        return perimeter
