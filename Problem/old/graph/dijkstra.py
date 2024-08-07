from typing import List
from math import inf
from heapq import heappop, heappush


# https://leetcode.cn/problems/network-delay-time/solutions/2668220/liang-chong-dijkstra-xie-fa-fu-ti-dan-py-ooe8/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, d in times:
            g[x - 1].append((y - 1, d))

        dis = [inf] * n
        dis[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heappush(h, (new_dis, y))
        mx = max(dis)
        return mx if mx < inf else -1

 


# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[inf]*n for _ in range(n)]
        for a,b,w in edges:
            self.g[a][b] = w


    def addEdge(self, edge: List[int]) -> None:
        a,b,w = edge
        self.g[a][b] = w


    def shortestPath(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [inf]*n
        vis = [False]*n
        dis[start] = 0
        for _ in range(n): # dijkstra 算法，每次找到一个最小距离
            x = -1
            for i in range(n):
                if not vis[i] and (x==-1 or dis[i]<dis[x]):
                    x = i
            if x == -1 or dis[x] == inf: # 从start开始已经没有可以更新的了
                return -1
            if x == end: # 找到终点，提前退出
                return dis[x]
            vis[x] = True
            for y,w in enumerate(self.g[x]):
                if dis[y]>dis[x]+w:
                    dis[y] = dis[x]+w # 更新最短路长度


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(start,end)





# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        ans = [-1] * n
        ans[0] = 0
        
        path = [[] for _ in range(n)]
        for u, v, w in edges:
            path[u].append((v, w))
            path[v].append((u, w))
        
        q = [(0, 0)]
        while q:
            d, u = heappop(q)
            if ans[u] != d: continue
            for v, w in path[u]:
                if (ans[v] == -1 or d + w < ans[v]) and d + w < disappear[v]:
                    ans[v] = d + w
                    heappush(q, (ans[v], v))
        return ans


# https://leetcode.cn/problems/find-edges-in-shortest-paths
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