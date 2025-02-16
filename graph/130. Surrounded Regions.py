"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are 
    on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr = len(board)
        nc = len(board[0])
        src = []
        visited = set()
        r_c_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == nr - 1 or j == 0 or j == nc - 1:
                    if board[i][j] == "O":
                        src.append((i, j))
                        visited.add((i, j))
        
        while src:
            i, j = src.pop(0)
            for dr, dc in r_c_delta:
                r = i + dr
                c = j + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and board[r][c] == "O":
                    src.append((r, c))
                    visited.add((r, c))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
