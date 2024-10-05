"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is 
connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

class Solution:
    def buildGraph(self, edges):
        graph = {}
        for i in range(len(edges)):
            graph[i + 1] = []
            for j in range(len(edges[i])):
                if edges[i][j] == 1 and i != j:
                    graph[i + 1].append(j + 1)
        return graph

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.buildGraph(isConnected)
        count = 0
        visited = set()
        
        for node in graph:
            queue = [ node ]
            if node not in visited:
                while queue:
                    src = queue.pop(0)
                    visited.add(src)
                    for neighbour in graph[src]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                count += 1

        return count
