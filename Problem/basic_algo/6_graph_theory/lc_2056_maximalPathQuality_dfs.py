# https://leetcode.cn/problems/maximum-path-quality-of-a-graph
from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for u,v,t in edges:
            g[u].append((v,t))
            g[v].append((u,t))
        
        def dfs(u,time,val):
            if u==0:
                nonlocal ans
                ans = max(ans,val)
            for v,t in g[u]:
                if time+t <= maxTime:
                    if not visited[v]:
                        visited[v] = True
                        dfs(v,time+t,val+values[v])
                        visited[v] = False
                    else:
                        dfs(v,time+t,val)
        ans = 0
        visited = [False]*n
        visited[0] = True
        dfs(0,0,values[0])
        return ans