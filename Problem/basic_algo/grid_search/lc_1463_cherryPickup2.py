# Problem: 1463. Cherry Pickup II
from typing import List
from functools import cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def getValue(x,y1,y2):
            return grid[x][y1]+grid[x][y2] if y1!=y2 else grid[x][y1]


        @cache
        def dfs(x,y1,y2): # 两个人一起出发
            if x==m-1:
                return getValue(x,y1,y2)
            ans = 0
            for a in [y1-1,y1,y1+1]:
                for b in [y2-1,y2,y2+1]:
                    if 0<=a<n and 0<=b<n:
                        ans = max(ans,dfs(x+1,a,b))
            return ans + getValue(x,y1,y2)
        m,n = len(grid),len(grid[0]) 
        return dfs(0,0,n-1) 