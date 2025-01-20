"""
2661. First Completely Painted Row or Column
https://leetcode.com/problems/first-completely-painted-row-or-column/

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

Example 1:
image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

Example 2:
image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        idx_dict = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                idx_dict[mat[i][j]] = (i, j)
        
        row_freq = {}
        for i in range(len(mat)):
            row_freq[i] = 0
        
        col_freq = {}
        for i in range(len(mat[0])):
            col_freq[i] = 0
        
        for ele in arr:
            i, j = idx_dict[ele]
            row_freq[i] += 1
            col_freq[j] += 1
            if row_freq[i] == len(mat[0]) or col_freq[j] == len(mat):
                return arr.index(ele)
