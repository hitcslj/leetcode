from typing import List
from math import inf

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