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
        row_size = len(board)
        col_size = len(board[0])
        start_index = []

        for i in range(row_size):
            for j in range(col_size):
                if board[i][j] == "O":
                    start_index.append([i, j])
        
        for i, j in start_index:
            flag = False
            indexes = []
            queue = [[i, j]]
            visited = set()
            pos = str(i) + "," + str(j)
            visited.add(pos)

            while len(queue) > 0:
                row, col = queue.pop(0)
                if row == 0 or col == 0 or row == row_size - 1 or col == col_size -1:
                    flag = True
                    break
                indexes.append([row, col])
                r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in r_c_delta:
                    r = row + dr
                    c = col + dc
                    pos = str(r) + "," + str(c)
                    if (0 <= r < row_size) and (0 <= c < col_size) and (pos not in visited) and (board[r][c] == "O"):
                        visited.add(pos)
                        queue.append([r, c])
            if not flag:
                for row, col in indexes:
                    board[row][col] = "X"
