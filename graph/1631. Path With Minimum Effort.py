"""
1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
"""

# Dijkstra's Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_len = len(heights) - 1
        col_len = len(heights[0]) - 1
        effort = [[float("inf")] * len(heights[0]) for _ in range(len(heights))]
        effort[0][0] = 0

        queue = [(0, 0)]
        r_c_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            i, j = queue.pop(0)
            for r, c in r_c_delta:
                row = i + r
                col = j + c
                if 0 <= row <= row_len and 0 <= col <= col_len:
                    new_effort = max(effort[i][j], abs(heights[i][j] - heights[row][col]))
                    if new_effort < effort[row][col]:
                        queue.append((row, col))
                        effort[row][col] = new_effort
        
        return effort[row_len][col_len]
