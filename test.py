from typing import List
from collections import Counter

class UnionFind:
    __slots__ = "p", "size"

    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

    def get_size(self, root: int) -> int:
        return self.size[root]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                graph[i][j] and uf.union(i, j)
        cnt = Counter(uf.find(x) for x in initial)
        ans, mx = n, 0
        for x in initial:
            root = uf.find(x)
            if cnt[root] > 1:
                continue
            sz = uf.get_size(root)
            if sz > mx or (sz == mx and x < ans):
                ans = x
                mx = sz
        return min(initial) if ans == n else ans