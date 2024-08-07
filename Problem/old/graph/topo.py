from typing import List
from collections import deque



# https://leetcode.cn/problems/parallel-courses
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in relations:
            g[x - 1].append(y - 1)
            deg[y - 1] += 1
        q = deque([i for i in range(n) if deg[i] == 0])
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                x = q.popleft()
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 0:
                        q.append(y)
        return ans if all(x == 0 for x in deg) else -1
        