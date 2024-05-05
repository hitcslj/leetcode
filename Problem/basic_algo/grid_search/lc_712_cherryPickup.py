# https://leetcode.cn/problems/cherry-pickup
from typing import List
from functools import cache
from math import inf

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(x1,y1,x2,y2): # 两个人一起出发，x1+y1 == x2+y2
            if x1==n-1 and y1==n-1:
                return grid[x1][y1]
            ans = -inf
            for a,b in [(x1+1,y1),(x1,y1+1)]:
                for c,d in [(x2+1,y2),(x2,y2+1)]:
                    if 0<=a<n and 0<=b<n and 0<=c<n and 0<=d<n and grid[a][b]!=-1 and grid[c][d]!=-1:
                        ans = max(ans,dfs(a,b,c,d))
            return ans + grid[x1][y1]+grid[x2][y2] if x1!=x2 or y1!=y2 else ans + grid[x1][y1]
        n = len(grid)
        ans = dfs(0,0,0,0)
        return ans if ans != -inf else 0
        