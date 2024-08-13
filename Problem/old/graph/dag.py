# https://leetcode.cn/problems/detonate-the-maximum-bombs
from typing import List
from functools import cache

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i, (x, y, r) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                dx = x - x2
                dy = y - y2
                if j != i and dx * dx + dy * dy <= r * r:
                    g[i].append(j)  # i 可以引爆 j

        def dfs(x: int) -> int:
            vis[x] = True
            cnt = 1
            for y in g[x]:
                if not vis[y]:
                    cnt += dfs(y)
            return cnt

        ans = 0
        for i in range(n):
            vis = [False] * n
            ans = max(ans, dfs(i))
        return ans


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        @cache
        def cachedKnows(a, b):
            return knows(a, b)

        def is_celebrity(i):
            for j in range(n):
                if i == j: continue
                if cachedKnows(i, j) or not cachedKnows(j, i):
                    return False
            return True
        
        celebrity_candidate = 0
        for i in range(1,n):
            if cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

        