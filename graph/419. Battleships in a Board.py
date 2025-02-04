"""
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleships = 0
        visited = set()
        r_c_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i, j) not in visited:
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)
                        for row, col in r_c_delta:
                            r = x + row
                            c = y + col
                            if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and board[r][c] == "X":
                                queue.append((r, c))
                                visited.add((r, c))
                    
                    battleships += 1
        
        return battleships
