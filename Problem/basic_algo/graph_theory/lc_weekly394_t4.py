# https://leetcode.cn/problems/find-edges-in-shortest-paths
from typing import List
from heapq import heappop, heappush
from math import inf

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        path = [[] for _ in range(n)]
        for u, v, w in edges:
            path[u].append((v, w))
            path[v].append((u, w))
        
        dist0 = [inf] * n
        dist0[0] = 0
        hpq = [(0, 0)]
        while hpq:
            d, u = heappop(hpq)
            if dist0[u] != d: continue
            for v, w in path[u]:
                if d + w < dist0[v]:
                    dist0[v] = d + w
                    heappush(hpq, (d + w, v))
        
        dist1 = [inf] * n
        dist1[n - 1] = 0
        hpq = [(0, n - 1)]
        while hpq:
            d, u = heappop(hpq)
            if dist1[u] != d: continue
            for v, w in path[u]:
                if d + w < dist1[v]:
                    dist1[v] = d + w
                    heappush(hpq, (d + w, v))
        
        if dist0[-1] == inf: return [False] * len(edges)
        return [dist0[u] + dist1[v] + w == dist0[-1] or dist0[v] + dist1[u] + w == dist0[-1] for u, v, w in edges]