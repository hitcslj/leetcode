# https://leetcode.cn/problems/detonate-the-maximum-bombs
from typing import List

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