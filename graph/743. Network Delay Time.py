"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

class Solution:
    def build_graph(self, times):
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = []
            graph[time[0]].append((time[1], time[2]))
            if time[1] not in graph:
                graph[time[1]] = []
        return graph

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX_TIME = 99999
        graph = self.build_graph(times)
        if len(graph[k]) == 0:
            return -1
        
        delay_time = {}
        for i in range(1, n + 1):
            if i not in graph:
                return - 1
            delay_time[i] = MAX_TIME
        
        queue = [(k, 0)]
        delay_time[k] = 0
        while queue:
            src, t = queue.pop(0)
            for neighbour, time in graph[src]:
                if delay_time[neighbour] > t + time:
                    delay_time[neighbour] = t + time
                    queue.append((neighbour, delay_time[neighbour]))
        
        min_time = 0
        for key in delay_time:
            if delay_time[key] == MAX_TIME:
                return -1
            min_time = max(min_time, delay_time[key])
        
        return min_time
