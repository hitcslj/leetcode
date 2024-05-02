# https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/

from typing import List
from collections import defaultdict, Counter

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
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ## 并查集
        n = len(nums)
        uf = UnionFind(n)
        rank = sorted(range(n),key=lambda x:nums[x])
        for i in range(1,n):
            if nums[rank[i]]-nums[rank[i-1]]<=limit:
                uf.merge(rank[i],rank[i-1])
        cnt = defaultdict(list)
        for i,pa in enumerate(uf.pa):
            cnt[pa].append(i) # 把可以交换的放到一个联通块里
        newNums = nums[:]
        for arr in cnt.values():
            newArr = sorted(arr,key=lambda x:nums[x])
            for i in range(len(arr)):
                newNums[arr[i]] = nums[newArr[i]]
        return newNums




    
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

# https://leetcode.cn/problems/minimize-malware-spread
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

# https://leetcode.cn/problems/minimize-malware-spread-ii
# 暴力算法
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        ans, mi = n, n
        for x in initial:
          uf = UnionFind(n)
          for i in range(n):
              for j in range(i + 1, n):
                  if graph[i][j] and i != x and j != x:
                      uf.union(i, j)
          cnt = set(uf.find(num) for num in initial if num!=x)
          sz = sum(uf.get_size(key) for key in cnt) # 被感染的节点数
          if sz < mi or (sz == mi and x < ans):
              ans = x
              mi = sz
        return min(initial) if ans == n else ans

# 逆向思维，找到能够感染最多节点的节点（且cnt[root]==1, 连接的感染源之后一个）
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        s = set(initial)
        uf = UnionFind(n)
        for i in range(n):
            if i not in s:
                for j in range(i + 1, n):
                    graph[i][j] and j not in s and uf.union(i, j)

        g = defaultdict(set)
        cnt = Counter()
        for i in initial:
            for j in range(n):
                if j not in s and graph[i][j]:
                    g[i].add(uf.find(j))
            for root in g[i]:
                cnt[root] += 1

        ans, mx = 0, -1
        for i in initial:
            t = sum(uf.get_size(root) for root in g[i] if cnt[root] == 1)
            if t > mx or (t == mx and i < ans):
                ans, mx = i, t
        return ans