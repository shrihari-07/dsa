"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel 
image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same 
color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [[sr, sc]]
        init_color = image[sr][sc]
        visited = set()
        row_size = len(image)
        col_size = len(image[0])
        image[sr][sc] = color

        while len(stack) > 0:
            x, y = stack.pop()
            r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            pos = str(x) + "," + str(y)

            if pos not in visited:
                visited.add(pos)
                for row, col in r_c_delta:
                    r = x + row
                    c = y + col
                    if (0 <= r < row_size) and (0 <= c < col_size) and image[r][c] == init_color:
                        image[r][c] = color
                        stack.append([r, c])
        
        return image
