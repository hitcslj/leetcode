# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from typing import List
from math import inf


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[inf] * n for _ in range(n)]
        for a, b, w in edges:
            g[a][b] = g[b][a] = w

        for k in range(n):
            g[k][k] = 0
            for i in range(n):
                for j in range(n):
                    # g[i][j] = min(g[i][j], g[i][k] + g[k][j])
                    if g[i][k] + g[k][j] < g[i][j]:
                        g[i][j] = g[i][k] + g[k][j]

        ans, cnt = n, inf
        for i in range(n - 1, -1, -1):
            t = sum(d <= distanceThreshold for d in g[i])
            if t < cnt:
                cnt, ans = t, i
        return ans
        
