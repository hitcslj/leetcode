# https://leetcode.cn/problems/optimize-water-distribution-in-a-village
from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.pa = list(range(n))
        self.size = n

    def find(self,x):
        if x!=self.pa[x]:
            self.pa[x]=self.find(self.pa[x])
        return self.pa[x]
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.pa[root_x] = root_y
            self.size-=1

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = []
        for i in range(n):
            edges.append((0,i+1,wells[i]))
        for u,v,cost in pipes:
            edges.append((u,v,cost))
        uf = UnionFind(n+1)
        edges.sort(key=lambda x:x[2])
        res = 0
        for u,v,cost in edges:
            if uf.find(u)!=uf.find(v):
                uf.merge(u,v)
                res+=cost
        return res

        
        
